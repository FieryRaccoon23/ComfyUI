from __future__ import annotations

import hashlib
import time
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np
import requests

from . import agent_runtime_info
from . import ollama_config
from . import ollama_embedding_util

def _sha256(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def _atomic_write_text(path: Path, text: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


def _atomic_write_npy(path: Path, arr: np.ndarray) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    np.save(tmp, arr)
    saved = tmp if tmp.suffix == ".npy" else Path(str(tmp) + ".npy")
    saved.replace(path)


# def _extract_type(t: Any) -> str:
#     if isinstance(t, str):
#         return t
#     if isinstance(t, (list, tuple)) and t and isinstance(t[0], str):
#         return t[0]
#     return "UNKNOWN"


# def _node_base_text(node_class: str, meta: Dict[str, Any]) -> str:
#     inp = meta.get("input", {}) or {}
#     req = (inp.get("required") or {})
#     opt = (inp.get("optional") or {})
#     hid = (inp.get("hidden") or {})

#     def fmt_inputs(d: Dict[str, Any]) -> str:
#         parts = []
#         for k in sorted(d.keys()):
#             parts.append(f"{k}:{_extract_type(d[k])}")
#         return ", ".join(parts)

#     outputs = meta.get("output") or meta.get("return_types") or meta.get("outputs") or []
#     if isinstance(outputs, str):
#         outputs = [outputs]

#     display = meta.get("display_name") or meta.get("name") or ""
#     category = meta.get("category") or ""
#     desc = meta.get("description") or meta.get("tooltip") or ""

#     # Keep stable + compact (avoid huge dumps)
#     return "\n".join([
#         f"class: {node_class}",
#         f"display: {display}",
#         f"category: {category}",
#         f"required: {fmt_inputs(req)}",
#         f"optional: {fmt_inputs(opt)}",
#         f"hidden: {fmt_inputs(hid)}",
#         f"outputs: {', '.join(map(str, outputs))}",
#         f"description: {desc}".strip(),
#     ]).strip()

def fetch_object_info_with_retry(url: str, *, attempts: int = 30, delay: float = 0.5, timeout: float = 10.0) -> dict | None:
    last_err = None
    for _ in range(attempts):
        try:
            r = requests.get(url, timeout=timeout)
            if r.status_code == 200:
                return r.json()
            last_err = RuntimeError(f"HTTP {r.status_code}")
        except Exception as e:
            last_err = e
        time.sleep(delay)
    print(f"[Embeddings] object_info not ready: {url} ({last_err})")
    return None

def compact_node_text(node_class: str, meta: dict) -> str:
    desc = (meta.get("description") or "").strip()

    output_tooltips = meta.get("output_tooltips") or []

    # normalize if someone stored strings instead of lists
    # if isinstance(output_tooltips, str):
    #     output_tooltips = [output_tooltips]

    #out_tips_line = " | ".join(str(x).strip() for x in output_tooltips if str(x).strip())
    out_tips_line = "\n".join(str(t) for t in output_tooltips if t is not None).strip()

    parts = []
    
    if desc:
        parts.append(f"{desc}")
    if out_tips_line:
        parts.append(f"{out_tips_line}")

    text = "\n".join(parts).strip()
    return text

def ensure_index_from_object_info() -> None:
    cache_dir = Path(__file__).resolve().parent / ollama_config.nodes_cache_directory

    cache_dir.mkdir(parents=True, exist_ok=True)

    gen_snapshot = cache_dir / "object_info.generated.json"
    custom_path = cache_dir / "node_custom_notes.json"
    web_crawler_path = cache_dir / "node_webcrawler_info.json"
    nodes_path = cache_dir / "node_index.nodes.json"
    meta_path = cache_dir / "node_index.meta.json"
    vecs_path = cache_dir / "node_index.vectors.npy"
    weights_path = cache_dir / "node_index.weights.npy"
    node_weights_path = cache_dir / "node_index.weights.json"
    node_final_texts_path = cache_dir / "node_index.final_texts.json"

    if custom_path.exists():
        custom_notes = json.loads(custom_path.read_text(encoding="utf-8"))
    else:
        custom_notes = {}

    if web_crawler_path.exists():
        web_crawler_notes = json.loads(web_crawler_path.read_text(encoding="utf-8"))
    else:
        web_crawler_notes = {}

    # Load old index if present
    old_meta = {}
    old_nodes: List[str] = []
    old_vecs = None
    if meta_path.exists() and nodes_path.exists() and vecs_path.exists():
        try:
            old_meta = json.loads(meta_path.read_text(encoding="utf-8"))
            old_nodes = json.loads(nodes_path.read_text(encoding="utf-8"))
            old_vecs = np.load(vecs_path)
        except Exception:
            old_meta, old_nodes, old_vecs = {}, [], None

    ollama_host = ollama_config.ollama_host
    embed_model = ollama_config.embed_model

    old_embed_model = old_meta.get("embed_model")
    reuse_allowed = (old_vecs is not None) and (old_embed_model == embed_model)

    old_hashes = old_meta.get("final_hashes", {}) or {}
    old_vec_map = {}
    if reuse_allowed:
        for i, n in enumerate(old_nodes):
            if i < len(old_vecs):
                old_vec_map[n] = old_vecs[i]

    obj_info_path = "/object_info"
    comfyUI_host_obj_info = f"{agent_runtime_info.comfy_ui_host}{obj_info_path}"
    object_info = fetch_object_info_with_retry(comfyUI_host_obj_info)
    if object_info is None:
        return

    # Build stable list of nodes (merge list from app and from web)
    node_names = sorted(set(object_info.keys()) | set(web_crawler_notes.keys()))

    final_hashes: Dict[str, str] = {}
    new_vecs: List[np.ndarray] = []
    new_weights: List[np.float32] = []
    node_weights: dict[str, float] = {}
    final_text_dict: dict[str, float] = {}
    reused = updated = 0

    for n in node_names:
        meta = object_info.get(n, {}) or {}
        base_text = compact_node_text(n, meta)
        user_text = (custom_notes.get(n) or "").strip()
        web_crawler_text = (web_crawler_notes.get(n) or "").strip()

        final_text = base_text
        if user_text:
            final_text += user_text
        if web_crawler_text:
            final_text += web_crawler_text

        # If no description, keep the weight lower
        decrease_weight = False
        if not final_text.strip():
            final_text = meta.get("name") or meta.get("display_name") or n
            decrease_weight = True
            
        w = np.float32(0.2 if decrease_weight else 1.0)
        new_weights.append(w)
        node_weights[str(n)] = float(w)

        final_text_dict[str(n)] = str(final_text)

        final_hash = _sha256(final_text)
        final_hashes[n] = final_hash

        if reuse_allowed and old_hashes.get(n) == final_hash and n in old_vec_map:
            new_vecs.append(old_vec_map[n])
            reused += 1
        else:
            v = np.array(ollama_embedding_util._embed(ollama_host, embed_model, final_text), dtype=np.float32)
            new_vecs.append(v)
            updated += 1

    if updated == 0:
        print("[Embeddings] Index already up to date; skipping write.")
        return
    else:
        print("[Embeddings] Will be building index.")

    vec_arr = np.stack(new_vecs, axis=0) if new_vecs else np.zeros((0, 0), dtype=np.float32)
    weight_arr = np.asarray(new_weights, dtype=np.float32)

    # Sanity check for vectors
    if vec_arr.ndim != 2 or vec_arr.shape[0] != len(node_names) or vec_arr.shape[1] == 0:
        print(f"[Embeddings] WARNING: Embedding matrix shape looks wrong: {vec_arr.shape}")
    else:
        bad = int(np.isnan(vec_arr).sum() + np.isinf(vec_arr).sum())
        if bad:
            print(f"[Embeddings] WARNING: Embeddings contain NaN/Inf values! bad_count={bad}")
        else:
            norms = np.linalg.norm(vec_arr, axis=1)
            zeroish = int((norms < 1e-8).sum())
            print(
                f"[Embeddings] Embeddings sanity OK. min_norm={norms.min():.4f} "
                f"max_norm={norms.max():.4f} zeroish={zeroish}"
            )

    # Save generated snapshot (optional but handy for debugging)
    _atomic_write_text(gen_snapshot, json.dumps(object_info, indent=2))

    # Save index
    _atomic_write_text(nodes_path, json.dumps(node_names, indent=2))
    _atomic_write_text(node_weights_path, json.dumps(node_weights, indent=2, sort_keys=True))
    _atomic_write_text(node_final_texts_path, json.dumps(final_text_dict, indent=2, sort_keys=True))
    _atomic_write_npy(vecs_path, vec_arr)
    _atomic_write_npy(weights_path, weight_arr)
    _atomic_write_text(meta_path, json.dumps({
        "embed_model": embed_model,
        "ollama_host": ollama_host,
        "count": len(node_names),
        "dim": int(vec_arr.shape[1]) if vec_arr.ndim == 2 else 0,
        "updated": updated,
        "reused": reused,
        "final_hashes": final_hashes,
    }, indent=2))

    print(
    f"[Embeddings] Node index build complete. nodes={len(node_names)} "
    f"updated={updated} reused={reused} dim={int(vec_arr.shape[1]) if vec_arr.ndim==2 else 0} "
    f"cache_dir={cache_dir}")
    print(f"[Embeddings] Wrote: {gen_snapshot.name}, {nodes_path.name}, {meta_path.name}, {vecs_path.name}")

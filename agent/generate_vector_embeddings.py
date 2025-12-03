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

def _parse_param_spec(spec):
    """
    spec is usually: [TYPE_OR_OPTIONS, CONFIG_DICT?]
      - TYPE_OR_OPTIONS can be "INT"/"FLOAT"/"STRING"/"COMBO"/etc OR a list of options
      - CONFIG_DICT can have tooltip/default/min/max/step/options/etc
    """
    param_type = None
    cfg = {}
    options = None

    if isinstance(spec, list) and spec:
        first = spec[0]
        if len(spec) > 1 and isinstance(spec[1], dict):
            cfg = spec[1]

        # If first is a list => it's a combo options list
        if isinstance(first, list):
            param_type = "COMBO"
            options = first
        else:
            param_type = str(first)

        # COMBO sometimes stores choices in cfg["options"] instead
        if param_type == "COMBO" and isinstance(cfg.get("options"), list):
            options = cfg["options"]

    elif isinstance(spec, str):
        param_type = spec

    return param_type, cfg, options


def _format_param(name, spec):
    param_type, cfg, options = _parse_param_spec(spec)

    tooltip = (cfg.get("tooltip") or "").strip()
    default = cfg.get("default", None)

    bits = [f"{name}: {param_type}" if param_type else name]
    if tooltip:
        bits.append(tooltip)
    if default is not None:
        bits.append(f"default={default}")

    # common numeric constraints
    for k in ("min", "max", "step", "round"):
        if k in cfg:
            bits.append(f"{k}={cfg[k]}")

    if options:
        # keep it short-ish; you can remove the slice if you want all
        bits.append("options=" + ", ".join(map(str, options[:50])) + ("..." if len(options) > 50 else ""))

    return " | ".join(bits)


def object_info_node_text(node_class: str, meta: dict) -> str:
    parts = []

    # high-level node info
    display_name = (meta.get("display_name") or "").strip()
    desc = (meta.get("description") or "").strip()
    if display_name and display_name != node_class:
        parts.append(display_name)
    if desc:
        parts.append(desc)

    # inputs (required/optional/hidden)
    inputs = meta.get("input") or {}
    for section in ("required", "optional", "hidden"):
        params = inputs.get(section) or {}
        if not isinstance(params, dict) or not params:
            continue
        parts.append(f"\n[{section} inputs]")
        for pname, pspec in params.items():
            parts.append(_format_param(pname, pspec))

    # outputs
    out_types = meta.get("output") or []
    out_names = meta.get("output_name") or []
    out_tips  = meta.get("output_tooltips") or []

    if out_types:
        parts.append("\n[outputs]")
        for i, otype in enumerate(out_types):
            oname = out_names[i] if i < len(out_names) else None
            otip  = out_tips[i] if i < len(out_tips) else None
            line = f"{oname or f'out{i}'}: {otype}"
            if otip:
                line += f" | {str(otip).strip()}"
            parts.append(line)

    return "\n".join(p for p in parts if str(p).strip()).strip()

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
    node_object_info_texts_path = cache_dir / "node_index.object_info_texts.json"
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

    object_info_text_dict: dict[str, str] = {}
    final_hashes: Dict[str, str] = {}
    new_vecs: List[np.ndarray] = []
    new_weights: List[np.float32] = []
    node_weights: dict[str, float] = {}
    final_text_dict: dict[str, str] = {}
    reused = updated = 0

    for n in node_names:
        meta = object_info.get(n, {}) or {}
        base_text = object_info_node_text(n, meta)
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

        object_info_text_dict[str(n)] = str(base_text)
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
    _atomic_write_text(node_object_info_texts_path, json.dumps(object_info_text_dict, indent=2, sort_keys=True))
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

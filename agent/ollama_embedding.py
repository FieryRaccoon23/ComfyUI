import numpy as np
import json
from pathlib import Path
from datetime import datetime
#from agent import ollama_config
#from agent import ollama_embedding_util

import requests
from typing import List

def _embed(host: str, embed_model: str, text: str) -> List[float]:
    r = requests.post(
        f"{host.rstrip('/')}/api/embeddings",
        json={"model": embed_model, "prompt": text},
        timeout=120,
    )
    if not r.ok:
        raise RuntimeError(f"Ollama embeddings failed ({r.status_code}): {r.text[:1000]}")
    return r.json()["embedding"]

def _load_node_index(cache_dir: Path | None = None) -> tuple[list[str], np.ndarray, dict]:
    cache_dir = cache_dir or (Path(__file__).resolve().parent / "node_cache")

    nodes_path = cache_dir / "node_index.nodes.json"
    vecs_path = cache_dir / "node_index.vectors.npy"
    snapshot_path = cache_dir / "object_info.generated.json"
    weights_path = cache_dir / "node_index.weights.npy"

    if not nodes_path.exists() or not vecs_path.exists():
        raise FileNotFoundError(f"Missing index files in {cache_dir}. Run ensure_index_from_object_info() first.")

    nodes: list[str] = json.loads(nodes_path.read_text(encoding="utf-8"))
    vecs: np.ndarray = np.load(vecs_path)  # (N, D)

    weights = np.ones((len(nodes),), dtype=np.float32)
    if weights_path.exists():
        weights = np.load(weights_path).astype(np.float32, copy=False)

    snapshot = {}
    if snapshot_path.exists():
        snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))

    if vecs.ndim != 2 or len(nodes) != vecs.shape[0]:
        raise RuntimeError(f"Index shape mismatch: nodes={len(nodes)} vecs={vecs.shape}")
    if weights.shape != (len(nodes),):
        raise RuntimeError(f"Weights shape mismatch: nodes={len(nodes)} weights={weights.shape}")

    return nodes, vecs.astype(np.float32, copy=False), snapshot, weights


def _topk_cosine(vecs: np.ndarray, q_vec: np.ndarray, top_k: int):
    """
    Returns (idx, sims) where idx are indices into vecs/nodes and sims are cosine similarities.
    Includes explicit warning suppression for macOS Accelerate 'ghost' warnings.
    """
    # 1. Force Double Precision and Contiguous Memory
    #    (Helps stability on M-series chips)
    v = np.ascontiguousarray(vecs, dtype=np.float64)
    q = np.ascontiguousarray(q_vec, dtype=np.float64)

    # 2. Sanitize Inputs
    v = np.nan_to_num(v, nan=0.0, posinf=0.0, neginf=0.0)
    q = np.nan_to_num(q, nan=0.0, posinf=0.0, neginf=0.0)

    # 3. Normalize (with epsilon safety)
    eps = 1e-10
    v_norms = np.linalg.norm(v, axis=1, keepdims=True)
    q_norm = np.linalg.norm(q)

    # Prevent division by zero
    v_norms = np.maximum(v_norms, eps)
    q_norm = max(q_norm, eps)

    vn = v / v_norms
    qn = q / q_norm

    # 4. Dot Product with Context Manager to Silence Spurious Warnings
    #    The 'divide', 'over', 'invalid' warnings here are often false positives
    #    from the BLAS library on macOS when handling certain vector sizes.
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        # using np.dot can sometimes bypass the buggy path taken by @
        sims = np.dot(vn, qn)

    # 5. Final Result Sanity Check (clean up any artifacts)
    sims = np.nan_to_num(sims, nan=-1.0, posinf=-1.0, neginf=-1.0)

    # 6. Top-K Sorting
    k = int(top_k)
    if k <= 0:
        k = 1
    k = min(k, sims.shape[0])

    idx = np.argpartition(-sims, kth=k - 1)[:k]
    idx = idx[np.argsort(-sims[idx])]
    
    return idx, sims[idx]


def query_node_index(query: str, *, top_k: int = 10) -> list[tuple[str, float]]:
    nodes, vecs, snapshot, weights = _load_node_index()

    # Log Stats for Vectors
    log_text = (
        f"vecs: shape={vecs.shape}, "
        f"NaN={np.isnan(vecs).sum()}, "
        f"Inf={np.isinf(vecs).sum()}, "
        f"min_norm={np.linalg.norm(np.nan_to_num(vecs), axis=1).min():.4f}"
    )
    _log_line(log_text)

    # Generate Query Embedding
    raw_embed = _embed("http://127.0.0.1:11434", "nomic-embed-text", query)
    q_vec = np.array(raw_embed, dtype=np.float32)

    # Log Stats for Query Vector (Crucial for debugging invalid value warnings)
    q_norm = np.linalg.norm(q_vec)
    log_q_text = (
        f"query: '{query}' | "
        f"shape={q_vec.shape}, "
        f"NaN={np.isnan(q_vec).sum()}, "
        f"norm={q_norm:.4f}"
    )
    _log_line(log_q_text)

    # Run Search
    idx, sims = _topk_cosine(vecs, q_vec, top_k)

    penalized = sims * weights[idx]
    order = np.argsort(-penalized)
    idx = idx[order]
    sims = penalized[order]

    results: list[tuple[str, float]] = []
    for rank, (i, s) in enumerate(zip(idx.tolist(), sims.tolist()), start=1):
        node_class = nodes[i]
        meta = snapshot.get(node_class, {}) or {}
        display = meta.get("name") or meta.get("display_name") or node_class
        category = (meta.get("category") or "").strip()
        desc = (meta.get("description") or "").strip()

        extra = []
        if category:
            extra.append(f"category={category}")
        if desc:
            extra.append(f"desc={desc[:120]}{'...' if len(desc) > 120 else ''}")

        print(f"{rank:2d}. {node_class}  score={s:0.4f}  display={display}" + (f"  ({', '.join(extra)})" if extra else ""))
        results.append((node_class, float(s)))

    return results

def _log_line(line: str, filename: str = "query_results.log") -> None:
    log_path = Path(__file__).resolve().parent / filename
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path.open("a", encoding="utf-8").write(f"[{ts}] {line}\n")

if __name__ == "__main__":
    # super simple CLI usage:
    #   python -m your_package.ollama_node_index_from_object_info "edge detection node"
    import sys
    q = " ".join(sys.argv[1:]).strip() or "text annotate node"
    query_node_index(q, top_k=10)
    # nodes, _, _, _ = _load_node_index()
    # hits = [n for n in nodes if "edge" in n.lower() or "canny" in n.lower() or "sobel" in n.lower()]
    # print("edge-like nodes:", hits[:50])

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
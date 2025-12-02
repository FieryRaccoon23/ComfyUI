import requests
from pathlib import Path
from . import ollama_config

def list_models() -> set[str]:
    r = requests.get(f"{ollama_config.ollama_host}/api/tags", timeout=10)
    r.raise_for_status()
    data = r.json()
    return {m["name"] for m in data.get("models", [])}

def ensure_model(model: str) -> None:
    installed = list_models()
    candidates = {model, f"{model}:latest"} if ":" not in model else {model}
    if installed.intersection(candidates):
        return

    r = requests.post(
        f"{ollama_config.ollama_host}/api/pull",
        json={"model": model, "stream": False},
        timeout=60 * 60,
    )
    r.raise_for_status()

def ensure_models(models: list[str]) -> None:
    for m in models:
        ensure_model(m)

def pull_models() -> tuple[str, str]:
    chat_model = ollama_config.chat_model
    embed_model = ollama_config.embed_model
    ensure_models([chat_model, embed_model])

    return chat_model, embed_model


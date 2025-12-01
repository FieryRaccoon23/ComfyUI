import requests
import json
from pathlib import Path
from . import ollama_config

def list_models() -> set[str]:
    r = requests.get(f"{ollama_config.OLLAMA_HOST}/api/tags", timeout=10)
    r.raise_for_status()
    data = r.json()
    return {m["name"] for m in data.get("models", [])}

def ensure_model(model: str) -> None:
    installed = list_models()
    candidates = {model, f"{model}:latest"} if ":" not in model else {model}
    if installed.intersection(candidates):
        return

    r = requests.post(
        f"{ollama_config.OLLAMA_HOST}/api/pull",
        json={"model": model, "stream": False},
        timeout=60 * 60,
    )
    r.raise_for_status()

def ensure_models(models: list[str]) -> None:
    for m in models:
        ensure_model(m)

def pull_models() -> tuple[str, str]:
    here = Path(__file__).resolve().parent
    json_path = here / "ollama_models.json"
    config = json.loads(Path(json_path).read_text())
    chat_model = config["chat_model"]
    embed_model = config["embed_model"]
    ensure_models([chat_model, embed_model])

    return chat_model, embed_model


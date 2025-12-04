from ollama import chat
from . import ollama_model, ollama_config

def send_prompt(prompt: str) -> str:
    chat_model, embed_model = ollama_model.pull_models()
    resp = chat(
        model=chat_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        keep_alive=ollama_config.ollama_keep_alive_time
    )

    return resp["message"]["content"]
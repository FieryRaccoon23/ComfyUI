from ollama import chat
from . import ollama_model


def test_chat():
    chat_model, embed_model = ollama_model.pull_models()

    resp = chat(
        model=chat_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hello in one sentence and tell me 2 fun facts about tea."},
        ],
    )
    print("*****************************************************")
    print(resp["message"]["content"])
    print("*****************************************************")
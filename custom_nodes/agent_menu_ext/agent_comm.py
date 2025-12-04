from aiohttp import web
from server import PromptServer
from agent import ollama_chat

def send_prompt(text: str) -> str:
    output = ollama_chat.send_prompt(text)
    return output

@PromptServer.instance.routes.post("/agent_menu_ext/ask")
async def agent_ask(request: web.Request):
    try:
        data = await request.json()
        text = (data.get("text") or "").strip()
        return web.json_response({"answer": send_prompt(text)})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)

from __future__ import annotations
from ollama import chat
from . import ollama_model, ollama_config, ollama_embedding, agent_build_flow

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

    return resp["message"]["content"]# ollama_chat.py

import json
from pathlib import Path
from typing import List, Tuple, Dict, Any

from ollama import chat

from . import ollama_model, ollama_config
from .ollama_embedding import query_node_index


# ---------- Small helpers ----------

_NODE_TEXTS_CACHE: Dict[str, str] | None = None


def _get_chat_model() -> str:
    chat_model, _ = ollama_model.pull_models()
    return chat_model


def _chat_text(system: str, user: str) -> str:
    resp = chat(
        model=_get_chat_model(),
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        keep_alive=ollama_config.ollama_keep_alive_time,
    )
    return (resp.get("message", {}) or {}).get("content", "") or ""


def _load_node_texts() -> Dict[str, str]:
    """
    Loads node_cache/node_index.final_texts.json once.
    Expected format: { "Canny": "...", "LoadImage": "...", ... }
    """
    global _NODE_TEXTS_CACHE
    if _NODE_TEXTS_CACHE is not None:
        return _NODE_TEXTS_CACHE

    # Try config-based folder first, then fallback to "node_cache"
    base = Path(__file__).resolve().parent
    path = base / "node_cache" / "node_index.final_texts.json"

    if not path.exists():
        _NODE_TEXTS_CACHE = {}
        return _NODE_TEXTS_CACHE

    _NODE_TEXTS_CACHE = json.loads(path.read_text(encoding="utf-8")) or {}
    return _NODE_TEXTS_CACHE


def _clean_lines(text: str) -> List[str]:
    lines = []
    for raw in text.splitlines():
        s = raw.strip()
        if not s:
            continue
        # remove common list prefixes: "1) ", "1. ", "- ", "* "
        s = s.lstrip("-*•").strip()
        if len(s) >= 3 and s[0].isdigit():
            # crude: strip leading "1." / "1)" / "10."
            s = s.split(" ", 1)[-1] if " " in s else s
            s = s.lstrip(").").strip()
        if s:
            lines.append(s)
    return lines


# ---------- Step 1: split prompt into commands ----------

def split_into_commands(user_prompt: str, max_steps: int = 12) -> List[str]:
    system = (
        "You are an expert ComfyUI workflow planner.\n"
        "Convert the user's request into a minimal ordered list of atomic steps.\n"
        "Rules:\n"
        "- Output ONLY the steps, one per line.\n"
        "- No numbering, no bullets, no extra commentary.\n"
        "- Each step should be a short verb phrase (e.g., 'Load image', 'Detect edges', 'Preview image').\n"
        "- Keep it ComfyUI-focused.\n"
    )
    text = _chat_text(system, user_prompt)
    steps = _clean_lines(text)

    # Fallback if model output is weird
    if not steps:
        # super basic fallback: treat whole prompt as one step
        return [user_prompt.strip()]

    return steps[:max_steps]


# ---------- Step 2: select best node among embedding candidates ----------

def choose_best_node(command: str, candidates: List[Tuple[str, float]]) -> str:
    """
    candidates: [(node_class, score), ...] from query_node_index()
    returns: best node_class
    """
    if not candidates:
        return ""

    node_texts = _load_node_texts()

    # Build a compact candidate list with short excerpts for the LLM
    blocks = []
    for node_class, score in candidates:
        info = (node_texts.get(node_class) or "").strip()
        if len(info) > 700:
            info = info[:700] + "..."
        blocks.append(f"- {node_class} (score={score:.4f})\n  {info}")

    system = (
        "You are selecting the single best ComfyUI node for a specific step.\n"
        "Return ONLY the node_class exactly as given in the candidate list.\n"
        "No extra words.\n"
    )
    user = (
        f"Step: {command}\n\n"
        f"Candidates:\n" + "\n".join(blocks) + "\n\n"
        "Which ONE candidate node_class best matches the step?"
    )

    answer = _chat_text(system, user).strip()

    # Accept only exact candidate matches; otherwise fallback to top score
    allowed = {n for n, _ in candidates}
    if answer in allowed:
        return answer

    # Sometimes models add quotes/spaces
    answer2 = answer.strip().strip('"').strip("'")
    if answer2 in allowed:
        return answer2

    # Fallback: highest embedding score (first element is already ranked by your code)
    return candidates[0][0]


# ---------- Main pipeline ----------

def plan_to_nodes(user_prompt: str, *, top_k: int = 10) -> str:
    """
    Returns: "Node1 -> Node2 -> ... -> NodeN"
    """
    commands = split_into_commands(user_prompt)
    chosen_nodes: List[str] = []

    for cmd in commands:
        candidates = query_node_index(cmd, top_k=top_k) 
        best = choose_best_node(cmd, candidates)
        if best:
            chosen_nodes.append(best)

    return " -> ".join(chosen_nodes)

def send_to_build_flow(text: str):
    agent_dir  = Path(__file__).resolve().parent
    path = agent_dir  / "node_cache" / "object_info.generated.json"
    object_info = json.loads(path.read_text(encoding="utf-8"))
    wf = agent_build_flow.build_comfyui_ui_workflow(text, object_info, schema="1.0")
    
    comfy_root = agent_dir.parent
    agent_build_flow.save_into_comfyui_workflows(wf, comfy_root, "hownowbrowncow_workflow")

def send_prompt(prompt: str) -> str:
    system = "You are a helpful assistant."
    text =  plan_to_nodes(prompt)
    send_to_build_flow(text)
    return text

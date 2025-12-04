from __future__ import annotations

import json
import re
from typing import Any, Dict, List, Tuple, Optional
from pathlib import Path

PRIMITIVE_TYPES = {"INT", "FLOAT", "STRING", "BOOLEAN", "NUMBER"}


def parse_chain(expr: str) -> List[str]:
    parts = [p.strip() for p in re.split(r"\s*->\s*", expr.strip()) if p.strip()]
    if len(parts) < 2:
        raise ValueError("Need at least two nodes, e.g. 'LoadImage -> Canny -> PreviewImage'")
    return parts


def _first_type(entry: Any) -> Any:
    # object_info inputs are usually like ["IMAGE", {...}] or [["a","b","c"], {...}]
    if isinstance(entry, list) and entry:
        return entry[0]
    return entry


def _norm_types(t: Any) -> set[str]:
    if t is None:
        return set()
    if isinstance(t, list):
        return {str(x) for x in t}
    return {str(t)}


def _compatible(out_t: Any, in_t: Any) -> bool:
    return bool(_norm_types(out_t) & _norm_types(in_t))


def _iter_inputs_in_order(meta: dict) -> List[Tuple[str, Any, dict]]:
    inp = meta.get("input") or {}
    req = inp.get("required") or {}
    opt = inp.get("optional") or {}
    order = meta.get("input_order") or {}

    req_order = order.get("required") or list(req.keys())
    opt_order = order.get("optional") or list(opt.keys())

    out: List[Tuple[str, Any, dict]] = []
    for name in req_order:
        if name in req:
            entry = req[name]
            t = _first_type(entry)
            cfg = entry[1] if isinstance(entry, list) and len(entry) > 1 and isinstance(entry[1], dict) else {}
            out.append((name, t, cfg))
    for name in opt_order:
        if name in opt:
            entry = opt[name]
            t = _first_type(entry)
            cfg = entry[1] if isinstance(entry, list) and len(entry) > 1 and isinstance(entry[1], dict) else {}
            out.append((name, t, cfg))
    return out


def _iter_outputs(meta: dict) -> List[Tuple[str, Any]]:
    outs = meta.get("output") or []
    names = meta.get("output_name") or []
    result: List[Tuple[str, Any]] = []
    for i, t in enumerate(outs):
        nm = names[i] if i < len(names) and names[i] else (t[0] if isinstance(t, list) and t else str(t))
        result.append((nm, t))
    return result


def _is_widget_input(t: Any, cfg: dict) -> bool:
    # Heuristic: widgets usually have defaults/ranges or are primitive types or COMBO lists
    if isinstance(t, list):  # COMBO options list
        return True
    if str(t) in PRIMITIVE_TYPES:
        return True
    if any(k in cfg for k in ("default", "min", "max", "step", "multiline", "image_upload")):
        return True
    return False


def _default_widget_value(t: Any, cfg: dict) -> Any:
    if "default" in cfg:
        return cfg["default"]
    if isinstance(t, list) and t:
        return t[0]
    # fallback sensible empties
    if str(t) == "BOOLEAN":
        return False
    if str(t) in ("INT", "FLOAT", "NUMBER"):
        return 0
    return ""


def build_comfyui_ui_workflow(
    chain_expr: str,
    object_info: Dict[str, Any],
    *,
    schema: str = "1.0",  # "1.0" (new) or "0.4" (old)
    start_pos: Tuple[int, int] = (80, 120),
    dx: int = 360,
    node_size: Tuple[int, int] = (315, 190),
    widget_values_override: Optional[Dict[str, Any]] = None,  # node_type -> widgets_values
) -> Dict[str, Any]:
    chain = parse_chain(chain_expr)
    widget_values_override = widget_values_override or {}

    nodes: List[dict] = []
    links: List[Any] = []
    link_id = 1

    # Build nodes
    for idx, node_type in enumerate(chain):
        if node_type not in object_info:
            raise KeyError(
                f"Unknown node type '{node_type}'. "
                f"Make sure the string uses the exact keys from /object_info."
            )

        meta = object_info[node_type]
        node_id = idx + 1

        # Create ONLY connectable input sockets (widgets handled via widgets_values)
        inputs = []
        widget_defaults = []
        in_slot = 0
        for name, t, cfg in _iter_inputs_in_order(meta):
            if _is_widget_input(t, cfg):
                widget_defaults.append(_default_widget_value(t, cfg))
                continue
            inputs.append({"name": name, "type": t, "link": None, "slot_index": in_slot})
            in_slot += 1

        outputs = []
        for out_slot, (name, t) in enumerate(_iter_outputs(meta)):
            outputs.append({"name": name, "type": t, "links": [], "slot_index": out_slot})

        node = {
            "id": node_id,
            "type": node_type,  # ComfyUI uses this as the node class/type
            "pos": [start_pos[0] + idx * dx, start_pos[1]],
            "size": [node_size[0], node_size[1]],
            "flags": {"collapsed": False},
            "order": node_id,
            "mode": 0,
            "inputs": inputs,
            "outputs": outputs,
            "properties": {"Node name for S&R": node_type},
            "widgets_values": widget_values_override.get(node_type, widget_defaults),
        }
        nodes.append(node)

    # Connect sequentially
    for i in range(len(nodes) - 1):
        a = nodes[i]
        b = nodes[i + 1]

        # Find best (type-matching) output->input pair
        chosen = None
        for o_idx, outp in enumerate(a.get("outputs", [])):
            out_t = outp.get("type")
            for in_idx, inp in enumerate(b.get("inputs", [])):
                if inp.get("link") is not None:
                    continue
                if _compatible(out_t, inp.get("type")):
                    chosen = (o_idx, in_idx, out_t)
                    break
            if chosen:
                break

        # Fallback: first output -> first input (if present)
        if not chosen:
            if not a.get("outputs") or not b.get("inputs"):
                continue
            chosen = (0, 0, a["outputs"][0].get("type"))

        o_idx, in_idx, out_t = chosen
        a["outputs"][o_idx]["links"].append(link_id)
        b["inputs"][in_idx]["link"] = link_id

        if schema == "1.0":
            # v1.0 link objects :contentReference[oaicite:1]{index=1}
            links.append(
                {
                    "id": link_id,
                    "origin_id": a["id"],
                    "origin_slot": o_idx,
                    "target_id": b["id"],
                    "target_slot": in_idx,
                    "type": out_t,
                }
            )
        elif schema == "0.4":
            # v0.4 link arrays [id, origin_id, origin_slot, target_id, target_slot, type] :contentReference[oaicite:2]{index=2}
            links.append([link_id, a["id"], o_idx, b["id"], in_idx, out_t])
        else:
            raise ValueError("schema must be '1.0' or '0.4'")

        link_id += 1

    # Top-level workflow
    if schema == "1.0":
        wf = {
            "version": 1,
            "config": {"links_ontop": True, "align_to_grid": True},
            "state": {
                "lastGroupid": 0,
                "lastNodeId": len(nodes),
                "lastLinkId": link_id - 1,
                "lastRerouteId": 0,
            },
            "groups": [],
            "nodes": nodes,
            "links": links,
            "extra": {},
        }
    else:
        wf = {
            "last_node_id": len(nodes),
            "last_link_id": link_id - 1,
            "nodes": nodes,
            "links": links,
            "groups": [],
            "config": {"links_ontop": True, "align_to_grid": True},
            "extra": {},
        }

    return wf


def write_workflow_json(path: str, workflow: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(workflow, f, ensure_ascii=False, indent=2)

def save_into_comfyui_workflows(workflow: dict, comfy_root: Path, name: str) -> Path:
    wf_dir = comfy_root / "user" / "default" / "workflows"
    wf_dir.mkdir(parents=True, exist_ok=True)
    out_path = wf_dir / f"{name}.json"
    out_path.write_text(json.dumps(workflow, indent=2), encoding="utf-8")
    return out_path
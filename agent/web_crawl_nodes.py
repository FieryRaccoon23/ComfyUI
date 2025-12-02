import requests
import shutil
import asyncio, json, re
from pathlib import Path
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from datetime import datetime
from typing import Any

FULL_SCRAPE = False

CRAWLER_DATA_DIR = "web_crawler"
NODE_CACHE_DIR = "node_cache"
JSON_FILE_NAME = "node_webcrawler_info.json"

INDEX_URL = "https://comfyui-wiki.com/en/comfyui-nodes"
PREFIX = "https://comfyui-wiki.com/en/comfyui-nodes"

def slug_to_pascal(s: str) -> str:
    if not s:
        return ""
    parts = re.split(r"[-_\s]+", s.strip())
    parts = [p for p in parts if p]
    return "".join(p[:1].upper() + p[1:] for p in parts)

def _convert_keys(obj: Any, recursive: bool) -> Any:
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            nk = slug_to_pascal(k) if isinstance(k, str) else k
            if nk in out:
                raise ValueError(f"Key collision after conversion: {k!r} -> {nk!r}")
            out[nk] = _convert_keys(v, recursive) if recursive else v
        return out
    if recursive and isinstance(obj, list):
        return [_convert_keys(x, recursive) for x in obj]
    return obj

def convert_json_keys_to_pascal(input_path: str | Path, *, recursive: bool = False) -> list[Path]:
    input_path = Path(input_path)
    outputs: list[Path] = []

    def _convert_file(p: Path) -> Path:
        data = json.loads(p.read_text(encoding="utf-8"))
        converted = _convert_keys(data, recursive=recursive)
        out = p.with_name(p.stem + ".pascal.json")
        out.write_text(json.dumps(converted, ensure_ascii=False, indent=2), encoding="utf-8")
        return out

    if input_path.is_dir():
        for p in sorted(input_path.glob("*.json")):
            # skip outputs to avoid infinite re-processing
            if p.name.endswith(".pascal.json"):
                continue
            outputs.append(_convert_file(p))
    else:
        outputs.append(_convert_file(input_path))

    return outputs

def safe_folder_name(url: str) -> str:
    slug = url.rstrip("/").split("/")[-1] or "root"
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", slug)

def extract_lora_loader_with_qwen(md: str, model: str, endpoint: str = "http://localhost:11434") -> str:
    prompt = f"""
    Extract the INTRODUCTION text for the "Load LoRA" / "Lora Loader" node from this markdown.

    What to return:
    - The full explanatory block immediately after the H1 title (# ...), up to (but not including) the next "##" section.
    - Keep bullet points.
    - Keep markdown formatting.

    What to remove:
    1) Any phrase/sentence that says: "For more information, please refer to [Installing LoRA Models](...)" (remove it entirely).
    2) Any phrase like: "as shown below: ![...](...)" (remove that entire phrase and the image markdown).

    Do NOT include:
    - Breadcrumbs, dates, "Last updated", tags
    - Input/Output tables or anything after "## Input Types"/"## Output Types"

    Output JSON ONLY exactly:
    {{"text":"..."}}

    Markdown:
    <<<BEGIN_MD
    {md}
    END_MD>>>
    """.strip()

    r = requests.post(
        f"{endpoint}/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
            "format": "json",
            "options": {"temperature": 0},
        },
        timeout=180,
    )
    r.raise_for_status()

    obj = json.loads((r.json().get("response") or "").strip())
    text = (obj.get("text") or "").strip() if isinstance(obj, dict) else ""

     # deterministic cleanup (in case the model misses it)
    text = re.sub(
        r"\s*For more information,\s*please refer to\s*\[Installing LoRA Models\]\([^)]+\)\s*\n?",
        "\n",
        text,
        flags=re.IGNORECASE
    )
    text = re.sub(r"\n{3,}", "\n\n", text).strip()

    text = re.sub(r"(?m)^\s*\*\s+", "", text)

    text = " ".join(text.split())

    return text

def extract_description_with_qwen(md: str, model: str, endpoint: str = "http://localhost:11434") -> str:
    prompt = f"""
    Extract the node DESCRIPTION from this markdown.

    Definition of "description":
    - A short explanatory paragraph about what the node does.
    - NOT breadcrumbs, dates, "Last updated", tags, examples, or Input/Output tables.
    - NOT bullet metadata like Class name / Category / Output node.

    Where to find it (in priority order):
    1) Under the first section heading that contains: Documentation OR Functionality OR Overview.
    - If the section starts with bullet metadata and the description is appended on the same bullet line,
        extract only the text AFTER the value (e.g., after `No`/`False`/`True`).
    - Otherwise extract the first normal paragraph in that section.
    2) If none of those headings exist, extract the first meaningful paragraph AFTER the H1 title (# ...),
    and STOP before the next section heading like "## Input Types" or "## Output Types".

    Return JSON ONLY exactly in this shape:
    {{"description":"..."}}
    If not found: {{"description":""}}

    Markdown:
    <<<BEGIN_MD
    {md}
    END_MD>>>
    """.strip()

    r = requests.post(
        f"{endpoint}/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=180,
    )
    r.raise_for_status()
    text = (r.json().get("response") or "").strip()

    # Try strict JSON parse first
    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            return (obj.get("description") or "").strip()
    except Exception:
        pass

    # Fallback: grab first JSON object in the output, if the model added extra text
    m = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if m:
        try:
            obj = json.loads(m.group(0))
            if isinstance(obj, dict):
                return (obj.get("description") or "").strip()
        except Exception:
            pass

    return ""

async def crawl_web():
    root = Path(__file__).resolve().parent / CRAWLER_DATA_DIR
    root.mkdir(parents=True, exist_ok=True)

    browser_cfg = BrowserConfig(headless=True)
    index_cfg = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        exclude_external_links=True,
        remove_overlay_elements=True,
    )
    page_cfg = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        exclude_external_links=True,
        remove_overlay_elements=True,
        css_selector="main",
    )

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        idx = await crawler.arun(INDEX_URL, config=index_cfg)
        internal = (idx.links or {}).get("internal", [])
        (root / "comfyui_nodes.links.internal.json").write_text(
            json.dumps(internal, indent=2),
            encoding="utf-8",
        )

        urls = sorted({
        item["href"]
        for item in internal
        if isinstance(item, dict)
        and isinstance(item.get("href"), str)
        and item["href"].startswith(PREFIX)
        and item["href"].rstrip("/") != INDEX_URL.rstrip("/")   # ignore the index itself
        })

        node_info = {}
        count = 1
        total = len(urls)
        for url in urls:
            node_name = safe_folder_name(url)

            # Sampler is not a node but it webpage contains info on it
            if node_name == "sampler":
                continue

            out_dir = root / node_name
            out_dir.mkdir(parents=True, exist_ok=True)

            r = await crawler.arun(url, config=page_cfg)

            md = r.markdown or ""
            (out_dir / "page.md").write_text(md, encoding="utf-8")

            # lora text is very wild, tame it separately
            if node_name == "lora-loader":
                node_info[node_name] = extract_lora_loader_with_qwen(md, model="qwen3:8b")
            else:
                node_info[node_name] = extract_description_with_qwen(md, model="qwen3:8b")

            print(("OK " if r.success else "FAIL"), url)
            print(f"{count}/{total}")
            count += 1

        (root / JSON_FILE_NAME).write_text(
        json.dumps(node_info, indent=2, ensure_ascii=False),
        encoding="utf-8",
        )

def create_json_from_last_scrapping():
    root = Path(__file__).resolve().parent / CRAWLER_DATA_DIR
    info = {}
    count = 0
    for node_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        if node_dir.name == "sampler":
            continue

        md_path = node_dir / "page.md"
        if not md_path.exists():
            continue

        md = md_path.read_text(encoding="utf-8", errors="ignore")
        info[node_dir.name]  = extract_description_with_qwen(md, model="qwen3:8b")

        count += 1
        print(f"Extracted: {count} ----- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    (root / JSON_FILE_NAME).write_text(
        json.dumps(info, indent=2, ensure_ascii=False),
        encoding="utf-8",
        )

if __name__ == "__main__":
    if FULL_SCRAPE:
        asyncio.run(crawl_web())
    else:
        create_json_from_last_scrapping()

    # TODO: This is bad but for now it is fine since it is only run when doc update
    convert_json_keys_to_pascal(Path(__file__).resolve().parent / CRAWLER_DATA_DIR, recursive=False)

    # move to node_cache
    web_root   = Path(__file__).resolve().parent / CRAWLER_DATA_DIR   # web_crawler
    cache_root = Path(__file__).resolve().parent / NODE_CACHE_DIR     # node_cache
    cache_root.mkdir(parents=True, exist_ok=True)

    src = web_root / JSON_FILE_NAME
    dst = cache_root / JSON_FILE_NAME

    shutil.copy2(src, dst)

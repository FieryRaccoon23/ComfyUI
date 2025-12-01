from __future__ import annotations

import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Optional
from . import ollama_config

@dataclass(frozen=True)
class OllamaConfig:
    mode: str = "off"  # "off" | "auto" | "require"
    host: str = ollama_config.OLLAMA_HOST
    quiet: bool = True  # suppress serve logs if we spawn it


def _ollama_installed() -> bool:
    return shutil.which("ollama") is not None


def _ollama_running(host: str) -> bool:
    # Official docs: base URL is http://localhost:11434/api and /api/tags lists models. :contentReference[oaicite:2]{index=2}
    url = f"{host.rstrip('/')}/api/tags"
    try:
        with urllib.request.urlopen(url, timeout=0.5) as resp:
            return 200 <= resp.status < 300
    except (urllib.error.URLError, TimeoutError):
        return False


def _start_ollama_serve(quiet: bool) -> Optional[subprocess.Popen]:
    stdout = stderr = None
    if quiet:
        stdout = subprocess.DEVNULL
        stderr = subprocess.DEVNULL

    try:
        # start_new_session keeps it alive if parent exits; also avoids ctrl-c signals.
        return subprocess.Popen(
            ["ollama", "serve"],
            stdout=stdout,
            stderr=stderr,
            start_new_session=True,
        )
    except FileNotFoundError:
        return None


def ensure_ollama(cfg: OllamaConfig) -> bool:
    """
    Returns True if Ollama is available for use, else False.
    In 'require' mode, exits the app if Ollama isn't available.
    """
    mode = (cfg.mode or "off").lower()

    if mode == "off":
        return False

    if not _ollama_installed():
        msg = (
            "Ollama is not installed (or not on PATH). "
            "Install Ollama or run with --ollama off to disable LLM features."
        )
        if mode == "require":
            print(msg, file=sys.stderr)
            raise SystemExit(1)
        print(msg, file=sys.stderr)
        return False

    if _ollama_running(cfg.host):
        return True

    if mode == "auto" or mode == "require":
        proc = _start_ollama_serve(cfg.quiet)
        if proc is None:
            if mode == "require":
                print(
                    "Failed to start Ollama (ollama executable not found).",
                    file=sys.stderr,
                )
                raise SystemExit(1)
            return False

        # Poll until it's reachable (briefly), otherwise treat as failed.
        deadline = time.monotonic() + 3.0
        while time.monotonic() < deadline:
            if _ollama_running(cfg.host):
                return True
            time.sleep(0.1)

        if mode == "require":
            print(
                "Ollama was started but did not become reachable at /api/tags.",
                file=sys.stderr,
            )
            raise SystemExit(1)
        return False

    return False

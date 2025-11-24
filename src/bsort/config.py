"""Simple config helpers for bsort."""

from __future__ import annotations
from typing import Dict

def get_model_name(cfg: Dict) -> str:
    """Return model name from config dict."""
    return cfg.get("model", {}).get("name", "yolov8n")

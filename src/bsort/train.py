"""Training module for the bsort project.

This module provides a simple training interface to be expanded
with a real ML training pipeline (YOLO or custom model).

Functions:
    train(config): Run a training routine using the given configuration.
"""

from __future__ import annotations
from typing import Dict
import wandb


def train(config: Dict) -> None:
    """Run training procedure.

    Args:
        config (Dict): Configuration loaded from YAML (settings.yaml).

    Notes:
        This is a skeleton implementation. The real implementation
        will include:
        - dataset loading
        - YOLO model training
        - color-class relabel workflow
        - evaluation & metrics logging
        - saving trained weights
    """
    wandb.init(
        project=config["wandb"]["project"],
        entity=config["wandb"]["entity"],
        config=config,
    )

    print("\n[bsort] Starting training (skeleton)...")
    print("[bsort] Configuration loaded:")
    for k, v in config.items():
        print(f"  {k}: {v}")

    print("\n[bsort] Training logic will be implemented here...")
    wandb.finish()

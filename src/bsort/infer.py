"""Inference module for the bsort project.

This module handles running inference on a single image using
a trained model (YOLO or custom lightweight model).
"""

from __future__ import annotations
from typing import Dict
import cv2


def infer(config: Dict, image_path: str) -> None:
    """Run inference on a single image.

    Args:
        config (Dict): Pipeline configuration.
        image_path (str): Path to the input image.

    Notes:
        This is a placeholder implementation. The real pipeline will:
        - load trained YOLO model (or ONNX, TFLite, PyTorch model)
        - preprocess image
        - run forward pass
        - decode predictions
        - draw bounding boxes & color labels
        - save or display output result
    """
    print(f"\n[bsort] Running inference on: {image_path}")

    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    print("[bsort] Image successfully loaded.")
    print("[bsort] Model inference will be implemented here.")

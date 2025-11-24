"""Utility functions for bsort."""
from __future__ import annotations
from typing import Tuple
import cv2
import numpy as np

def crop_bbox(image: np.ndarray, bbox_rel: Tuple[float, float, float, float]) -> np.ndarray:
    """Crop bounding box from image using YOLO relative coords.

    Args:
        image: BGR image array.
        bbox_rel: (x_center, y_center, width, height) in relative [0,1] coords.

    Returns:
        Cropped BGR image as numpy array.
    """
    h, w = image.shape[:2]
    xc, yc, bw, bh = bbox_rel
    x1 = max(int((xc - bw/2) * w), 0)
    y1 = max(int((yc - bh/2) * h), 0)
    x2 = min(int((xc + bw/2) * w), w-1)
    y2 = min(int((yc + bh/2) * h), h-1)
    return image[y1:y2, x1:x2]

def mean_hsv(bgr_crop: np.ndarray) -> Tuple[float, float, float]:
    """Return mean HSV values of a BGR crop."""
    hsv = cv2.cvtColor(bgr_crop, cv2.COLOR_BGR2HSV)
    h_mean = float(hsv[:, :, 0].mean())
    s_mean = float(hsv[:, :, 1].mean())
    v_mean = float(hsv[:, :, 2].mean())
    return h_mean, s_mean, v_mean

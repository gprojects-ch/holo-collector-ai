# app/inference.py
from typing import Any, Dict, List

import numpy as np
from PIL import Image
from io import BytesIO

from .models.loader import model_registry


def load_image_from_bytes(data: bytes) -> np.ndarray:
  """JPEG/PNG-Bytes -> numpy-Array (RGB)."""
  img = Image.open(BytesIO(data)).convert("RGB")
  return np.array(img)


def run_fullbody_inference(image_bytes: bytes) -> Dict[str, Any]:
  """
  Führt Full-Body-Minifig-Erkennung auf CPU aus.
  Gibt ein dict zurück, das direkt als JSON serialisierbar ist.
  """
  model_info = model_registry.get("fullbody_v1")
  yolo_model = model_info.yolo

  img = load_image_from_bytes(image_bytes)

  # YOLO Inference
  results = yolo_model(
    img,
    verbose=False  # kein Spam im Log
  )

  detections: List[Dict[str, Any]] = []

  # results ist eine Liste (für Batch), wir haben nur 1 Bild
  res = results[0]

  if res.boxes is not None and len(res.boxes) > 0:
    boxes = res.boxes.xywh.cpu().numpy()      # [x_center, y_center, w, h]
    scores = res.boxes.conf.cpu().numpy()
    classes = res.boxes.cls.cpu().numpy().astype(int)

    img_h, img_w = img.shape[:2]

    for (cx, cy, w, h), score, cls_idx in zip(boxes, scores, classes):
      # YOLO xywh sind Pixel-Koordinaten bezogen aufs Input-Bild
      detections.append(
        {
          "class": model_info.info["classes"][cls_idx]
          if cls_idx < len(model_info.info.get("classes", []))
          else str(cls_idx),
          "classId": int(cls_idx),
          "confidence": float(score),
          "box": {
            "x": float(cx - w / 2.0),
            "y": float(cy - h / 2.0),
            "width": float(w),
            "height": float(h),
            "imageWidth": int(img_w),
            "imageHeight": int(img_h),
          },
        }
      )

  return {
    "model": {
      "id": model_info.id,
      "version": model_info.info.get("version"),
      "task": model_info.info.get("task"),
    },
    "detections": detections,
  }

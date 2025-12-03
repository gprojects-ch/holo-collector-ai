# app/models/loader.py
from pathlib import Path
from typing import Dict, Any

from ultralytics import YOLO
import json

BASE_DIR = Path(__file__).resolve().parents[2]  # Projekt-Root
MODELS_DIR = BASE_DIR / "models"


class ModelInfo:
  def __init__(self, model_id: str, info: Dict[str, Any], yolo_model: YOLO):
    self.id = model_id
    self.info = info
    self.yolo = yolo_model


class ModelRegistry:
  """
  Sehr simple Registry:
  - Lädt beim Start fullbody_v1
  - Später kannst du hier weitere Modelle eintragen
  """

  def __init__(self):
    self._models: Dict[str, ModelInfo] = {}
    self._load_fullbody_v1()

  def _load_fullbody_v1(self):
    model_id = "fullbody_v1"
    model_dir = MODELS_DIR / model_id
    weights_path = model_dir / "best.pt"
    info_path = model_dir / "modelinfo.json"

    if not weights_path.exists():
      raise FileNotFoundError(f"Model weights not found at {weights_path}")

    if not info_path.exists():
      raise FileNotFoundError(f"Model info not found at {info_path}")

    with info_path.open("r", encoding="utf-8") as f:
      info = json.load(f)

    # CPU-only
    yolo_model = YOLO(str(weights_path)).to("cpu")

    self._models[model_id] = ModelInfo(model_id, info, yolo_model)

  def get(self, model_id: str) -> ModelInfo:
    if model_id not in self._models:
      raise KeyError(f"Model {model_id} is not loaded")
    return self._models[model_id]


# globale Registry-Instanz
model_registry = ModelRegistry()

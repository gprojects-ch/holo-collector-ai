# app/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

from .inference import run_fullbody_inference

app = FastAPI(title="Holo-Collector AI", version="0.1.0")


@app.get("/health")
def health():
  return {"status": "ok"}


@app.post("/infer/minifigure-fullbody")
async def infer_minifigure_fullbody(file: UploadFile = File(...)):
  """
  Erwartet ein Bild als multipart/form-data (Feldname: file).
  Gibt Detections als JSON zurück.
  """
  if file.content_type not in ("image/jpeg", "image/png", "image/webp"):
    raise HTTPException(status_code=400, detail="Unsupported image type")

  image_bytes = await file.read()

  try:
    result = run_fullbody_inference(image_bytes)
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

  # Hier könntest du noch meta/perf etc. ergänzen
  return JSONResponse(result)

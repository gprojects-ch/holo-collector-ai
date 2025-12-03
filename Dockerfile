FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Systemabhängigkeiten für Pillow / OpenCV & Co.
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Requirements zuerst kopieren (für Schichten-Caching)
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Projekt-Code + Modelle kopieren
COPY app ./app
COPY models ./models

# Port für FastAPI
EXPOSE 8000

# Start FastAPI via uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

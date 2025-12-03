FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Requirements
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt \
    --extra-index-url https://download.pytorch.org/whl/cpu

# Ultralytics: ohne deps
RUN pip install --no-cache-dir ultralytics==8.3.1 --no-deps

# Benötigte Ultralytics-Abhängigkeiten
RUN pip install --no-cache-dir opencv-python-headless==4.9.0.80
RUN pip install --no-cache-dir psutil
RUN pip install --no-cache-dir matplotlib==3.7.2
RUN pip install --no-cache-dir tqdm

# Projekt
COPY app ./app
COPY models ./models

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

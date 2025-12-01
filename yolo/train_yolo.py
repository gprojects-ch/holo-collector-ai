from ultralytics import YOLO

def main():
    model = YOLO("yolo11s.pt")  # Base model

    model.train(
        data="/workspace/holo-collector-ai/yolo/data/data.yaml",
        imgsz=1024,
        epochs=80,
        batch=16,
        device=0,
        project="/workspace/holo-collector-ai/yolo/runs",
        name="minifig_baseline"
    )

if __name__ == "__main__":
    main()

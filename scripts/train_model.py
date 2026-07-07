from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="datasets/PPE_Dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    workers=2,
    project="models",
    name="SafeSight",
    pretrained=True,
    device="cpu"
)

print("Training Completed Successfully!")
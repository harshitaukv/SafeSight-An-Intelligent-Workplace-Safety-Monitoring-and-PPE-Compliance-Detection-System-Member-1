from ultralytics import YOLO

print("Loading YOLOv8 model...")

model = YOLO("yolov8n.pt")

print("YOLOv8 loaded successfully!")
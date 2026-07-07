import os

label_folder = "datasets/ConstructionSafety/labels"

count = 0

for file in os.listdir(label_folder):
    if file.endswith(".txt"):
        count += 1

print("YOLO Labels Created:", count)
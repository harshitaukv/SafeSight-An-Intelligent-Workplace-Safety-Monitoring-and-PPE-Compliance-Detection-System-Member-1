import os
import xml.etree.ElementTree as ET

# Dataset paths
IMAGE_DIR = "datasets/ConstructionSafety/images"
XML_DIR = "datasets/ConstructionSafety/annotations"
LABEL_DIR = "datasets/ConstructionSafety/labels"

os.makedirs(LABEL_DIR, exist_ok=True)

# Class mapping
classes = {
    "helmet": 0,
    "head": 1
}

def convert_bbox(size, box):
    width, height = size

    xmin, ymin, xmax, ymax = box

    x_center = ((xmin + xmax) / 2) / width
    y_center = ((ymin + ymax) / 2) / height

    box_width = (xmax - xmin) / width
    box_height = (ymax - ymin) / height

    return x_center, y_center, box_width, box_height

xml_files = [f for f in os.listdir(XML_DIR) if f.endswith(".xml")]

print(f"Found {len(xml_files)} XML files\n")

for xml_file in xml_files:

    xml_path = os.path.join(XML_DIR, xml_file)

    tree = ET.parse(xml_path)
    root = tree.getroot()

    width = int(root.find("size/width").text)
    height = int(root.find("size/height").text)

    txt_name = xml_file.replace(".xml", ".txt")
    txt_path = os.path.join(LABEL_DIR, txt_name)

    with open(txt_path, "w") as output:

        for obj in root.findall("object"):

            class_name = obj.find("name").text.lower()

            if class_name not in classes:
                continue

            class_id = classes[class_name]

            bbox = obj.find("bndbox")

            xmin = float(bbox.find("xmin").text)
            ymin = float(bbox.find("ymin").text)
            xmax = float(bbox.find("xmax").text)
            ymax = float(bbox.find("ymax").text)

            x, y, w, h = convert_bbox(
                (width, height),
                (xmin, ymin, xmax, ymax)
            )

            output.write(
                f"{class_id} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n"
            )

print("XML conversion completed successfully.")
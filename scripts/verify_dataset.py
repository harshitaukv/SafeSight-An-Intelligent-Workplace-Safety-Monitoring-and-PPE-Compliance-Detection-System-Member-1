import os

DATASET_PATH = "datasets"

print("=" * 60)
print("SafeSight Dataset Verification")
print("=" * 60)

for dataset in os.listdir(DATASET_PATH):

    path = os.path.join(DATASET_PATH, dataset)

    if not os.path.isdir(path):
        continue

    print("\nDataset :", dataset)

    total_images = 0
    total_xml = 0
    total_txt = 0

    for root, dirs, files in os.walk(path):

        for file in files:

            file = file.lower()

            if file.endswith((".jpg", ".jpeg", ".png")):
                total_images += 1

            elif file.endswith(".xml"):
                total_xml += 1

            elif file.endswith(".txt"):
                total_txt += 1

    print("Images :", total_images)
    print("XML :", total_xml)
    print("TXT :", total_txt)

print("\nVerification Completed")
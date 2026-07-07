import os

datasets = [

"datasets/ConstructionSafety",

"datasets/HardHat/css-data",

"datasets/PPEKit/data"

]

print("="*60)

print("SafeSight Dataset Inspector")

print("="*60)

for dataset in datasets:

    print("\nChecking:", dataset)

    image_count = 0
    label_count = 0

    for root, dirs, files in os.walk(dataset):

        for file in files:

            if file.endswith((".jpg",".jpeg",".png")):
                image_count += 1

            elif file.endswith(".txt"):
                label_count += 1

    print("Images :", image_count)
    print("Labels :", label_count)
import os

datasets = [
    "datasets/ConstructionSafety",
    "datasets/HardHat/css-data",
    "datasets/PPEKit/data"
]

for dataset in datasets:

    print("\n" + "=" * 60)
    print(dataset)
    print("=" * 60)

    classes = set()

    for root, dirs, files in os.walk(dataset):

        # Only read label folders
        if "labels" not in root.lower():
            continue

        for file in files:

            if not file.endswith(".txt"):
                continue

            path = os.path.join(root, file)

            with open(path, "r") as f:

                for line in f:

                    line = line.strip()

                    if line == "":
                        continue

                    values = line.split()

                    # Ignore README text
                    if len(values) != 5:
                        continue

                    classes.add(values[0])

    print("Classes Found:")
    print(sorted(classes))
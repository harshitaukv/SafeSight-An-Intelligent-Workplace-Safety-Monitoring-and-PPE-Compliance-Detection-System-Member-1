import os
from collections import Counter

label_root = "datasets/HardHat/css-data"

counter = Counter()

for root, dirs, files in os.walk(label_root):

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

                if len(values) != 5:
                    continue

                counter[int(values[0])] += 1

print("=" * 60)
print("Classes Found")
print("=" * 60)

for cls in sorted(counter):
    print(f"Class {cls} : {counter[cls]} objects")
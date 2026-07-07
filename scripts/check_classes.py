import os

DATASET = "datasets"

classes = set()

for root, dirs, files in os.walk(DATASET):

    for file in files:

        if file.endswith(".txt"):

            path = os.path.join(root, file)

            with open(path) as f:

                for line in f:

                    if len(line.strip()) == 0:
                        continue

                    cls = line.split()[0]

                    classes.add(cls)

print("Detected Class IDs")

print(classes)
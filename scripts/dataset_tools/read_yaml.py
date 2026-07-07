import os
import yaml

search_paths = [
    "datasets/HardHat",
    "datasets/PPEKit"
]

found = False

for base in search_paths:
    for root, dirs, files in os.walk(base):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                found = True
                path = os.path.join(root, file)

                print("=" * 60)
                print("Found:", path)
                print("=" * 60)

                with open(path, "r") as f:
                    data = yaml.safe_load(f)

                print(data)
                print()

if not found:
    print("No YAML files found.")
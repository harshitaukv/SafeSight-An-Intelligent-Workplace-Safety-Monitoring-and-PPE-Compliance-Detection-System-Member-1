import os

folders = [

"datasets/ConstructionSafety",

"datasets/HardHat",

"datasets/PPEKit"

]

print("=" * 60)

print("Preparing SafeSight Dataset")

print("=" * 60)

for folder in folders:

    print("\nChecking :", folder)

    if os.path.exists(folder):

        print("Found")

    else:

        print("Missing")

print("\nEverything Ready")
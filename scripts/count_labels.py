import os

count = 0

for root, dirs, files in os.walk("datasets"):

    for file in files:

        if file.endswith(".txt"):

            count += 1

print("Total Labels :", count)
import csv
counts = {}

with open("save.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Location"] in counts:
            counts[row["Location"]] += 1
        else:
            counts[row["Location"]] = 1

for count in sorted(counts, key=counts.get, reverse=True):
    print(f"{count}: {counts[count]}")
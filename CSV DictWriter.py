import csv

pass_count = 0

with open("CSV Example.csv", encoding="utf-8-sig") as infile, \
    open("High Ratings.csv", mode="w", newline="", encoding="utf-8") as outfile:

    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    while True:
        try:
            rating_thresh = int(input("Enter a minimum rating: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    for row in reader:
        if int(row["Rating"]) >= rating_thresh:
            writer.writerow(row)
            pass_count += 1

print(f"{pass_count} entries matched your criteria.")
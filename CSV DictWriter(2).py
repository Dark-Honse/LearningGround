import csv

pass_count = 0
fail_count = 0

with open("CSV Example.csv", encoding="utf-8-sig") as infile, \
    open("High Ratings.csv", "w", newline="", encoding="utf-8") as highfile, \
    open("Low Ratings.csv", "w", newline="", encoding="utf-8") as lowfile:
    reader = csv.DictReader(infile)
    fieldnames = (reader.fieldnames or []) + ["Status"]

    high_writer = csv.DictWriter(highfile, fieldnames=fieldnames)
    low_writer = csv.DictWriter(lowfile, fieldnames=fieldnames)

    high_writer.writeheader()
    low_writer.writeheader()

    while True:
        try:
            rating_thresh = int(input("Enter a minimum rating: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    for row in reader:
        if int(row["Rating"]) >= rating_thresh:
            row["Status"] = "A Team"
            pass_count += 1
            high_writer.writerow(row)
        else:
            row["Status"] = "Grunt"
            fail_count += 1
            low_writer.writerow(row)

    print(f"{pass_count} entries matched your criteria.")
    print(f"{fail_count} entries failed to match your criteria.")
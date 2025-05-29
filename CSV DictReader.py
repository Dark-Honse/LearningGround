import csv

total_age = 0
total_rating = 0
count = 0
oldest_age = 0
oldest_name = ""
youngest_age = 9999999
youngest_name = ""

with open("CSV Example.csv", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
        total_age += int(row["Age"])
        total_rating += int(row["Rating"])
        count += 1
        if int(row["Age"]) >= oldest_age:
            oldest_age = int(row["Age"])
            oldest_name = row["Name"]
        if int(row["Age"]) <= youngest_age:
            youngest_age = int(row["Age"])
            youngest_name = row["Name"]

    ave_age = total_age / count
    ave_rating = total_rating / count
    print(round(ave_age))
    print(round(ave_rating))
    print(f"{oldest_name} is the oldest at {oldest_age} years old.")
    print(f"{youngest_name} is the youngest at {youngest_age} years old.")
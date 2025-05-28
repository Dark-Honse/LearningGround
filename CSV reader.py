import csv

age_count= 0
total_age = 0
ave_age = 0
oldest = 0
name = ""

rating_count = 0
total_rating = 0
ave_rating = 0

with open("CSV Example.csv", encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    next(reader)
    data = list(reader)

    for row in data:
        print(row[1])
        total_age += int(row[1])
        age_count += 1

    ave_age = total_age / age_count

    print(total_age)
    print(round(ave_age))
    age_count = 0
    total_age = 0
    ave_age = 0

    print("--------------")

    for row in data:
        rating_count += 1
        total_rating += int(row[2])
    print(total_rating)
    print(rating_count)
    ave_rating = total_rating / rating_count
    print(ave_rating)
    print("-----------")

    ave_rating = 0
    rating_count = 0
    total_rating = 0

    for row in data:
        if int(row[2]) > 80:
            rating_count += 1
            total_rating += int(row[2])
    ave_rating = total_rating / rating_count
    print(round(ave_rating))

    ave_rating = 0
    rating_count = 0
    total_rating = 0

    print("--------------")
    for row in data:
        if int(row[1]) >= oldest:
            oldest = int(row[1])
            name = str(row[0])
    print(oldest)
    print(f"{name} is the oldest at {oldest} years old.")



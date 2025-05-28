import csv

age_count= 0
total_age = 0
ave_age = 0

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

    print("--------------")

    for row in data:
        rating_count += 1
        total_rating += int(row[2])
    print(total_rating)
    print(rating_count)
    ave_rating = total_rating / rating_count
    print(ave_rating)



import csv

with open("clean_sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["price"]) < 1000:
            print(row["product"], row["price"])

# Day 02: Sales Data Cleaner

import csv 

sales = [
    {"id": 1, "product": "Laptop", "qty": 1, "price": 45000},
    {"id": 2, "product": "Mouse", "qty": 2, "price": 500},
    {"id": 3, "product": "", "qty": 1, "price": 200},
    {"id": 2, "product": "Mouse", "qty": 2, "price": 500},
    {"id": 4, "product": "Monitor", "qty": 1, "price": -5000},
    {"id": 5, "product": "Keyboard", "qty": 0, "price": 1000}
]

clean_data = []
seen_ids = set()

for item in sales:

    # Step 1: Remove duplicate IDs
    if item["id"] in seen_ids:
        print("Duplicate removed:", item["id"])
        continue

    seen_ids.add(item["id"])

    # Step 2: Remove invalid records
    if not item["product"].strip() or item["qty"] <= 0 or item["price"] < 0:
        print("Invalid record removed:", item["id"])
        continue

    # Step 3: Calculate revenue
    item["revenue"] = item["qty"] * item["price"]

    # Step 4: Save valid record
    clean_data.append(item)

# Step 5: Calculate total revenue
total_revenue = 0

for item in clean_data:
    total_revenue += item["revenue"]

print("\n--- SALES REPORT ---")
print("Raw records:", len(sales))
print("Clean records:", len(clean_data))
print("Total revenue: ₹", total_revenue)

print("\nClean data:")
for item in clean_data:
    print(item)

# Save clean data to CSV file

with open("clean_sales.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["id", "product", "qty", "price", "revenue"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(clean_data)

print("Clean data saved to clean_sales.csv")

# Read and verify saved CSV file

print("\n--- VERIFY CSV FILE ---")

with open("clean_sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

# Data quality check

with open("clean_sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    saved_data = list(reader)

print("\n--- DATA QUALITY CHECK ---")
print("Expected records:", len(clean_data))
print("Saved records:", len(saved_data))

assert len(saved_data) == len(clean_data), "Record count mismatch!"

print("Data quality check passed!")        
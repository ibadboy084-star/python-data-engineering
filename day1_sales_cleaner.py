import csv
from pathlib import Path


sales = [
{"id": 1, "product": "Laptop", "qty": 1, "price": 45000},
{"id": 2, "product": "Mouse", "qty": 2, "price": 500},
{"id": 3, "product": "Keyboard", "qty": 1, "price": 1200},
{"id": 2, "product": "Mouse", "qty": 2, "price": 500},
{"id": 4, "product": "Monitor", "qty": 1, "price": -5000},
]

clean_data = []
seen_ids = set()

# Clean the data

for item in sales:
 if item["id"] in seen_ids:
  print("Duplicate removed:", item["id"])
   continue

 if not item["product"].strip() or item["qty"] <= 0 or item["price"] < 0:  
    print("Invalid record removed:", item["id"])  
     continue  

seen_ids.add(item["id"])  

clean_data.append({  
    "id": item["id"],  
    "product": item["product"],  
    "qty": item["qty"],  
    "price": item["price"],  
    "revenue": item["qty"] * item["price"]  
})

# Save cleaned data to CSV

output = Path(file).parent / "clean_sales.csv"

with output.open("w", newline="", encoding="utf-8") as file:
 columns = ["id", "product", "qty", "price", "revenue"]
 writer = csv.DictWriter(file, fieldnames=columns)
 writer.writeheader()
 writer.writerows(clean_data)

total = sum(item["revenue"] for item in clean_data)

print("\n--- SALES REPORT ---")
print("Raw records:", len(sales))
print("Clean records:", len(clean_data))
print("Total revenue: ₹", total)
print("CSV saved:", output)
# Level 1 — write sales_report.py that:

# Opens and reads the CSV file
# Counts total number of orders
# Calculates total and average of the amount column — skipping rows where amount is missing
# Prints this report:
# Total Orders: 8
# Orders with valid amount: 7
# Total sales: 2375.24
# Average sale: 339.32

# --- Data Quality Report ---
# Missing customer (1): ['1006']
# Missing amount (1): ['1002']
# Missing date (1): ['1004']
# Negative amount (1): ['1008']

import csv

# Initialize accumulators - empty lists to collect problem order_ids
missing_customer = []
missing_amount = []
missing_date = []
negative_amount = []

with open("sales.csv", "r") as file:
    # DictReader = built-in class that reads a CSV file and maps each row into a dictionary
    reader = csv.DictReader(file)  # Earlier had used csv.reader(file)
    # header = next(reader) # Skips the header row
    rows = list(reader)
    
    # Level 1 — existing calculations
    # row_count = sum(1 for row in reader)
    orders = sum(1 for row in rows if row["amount"].strip())
    # total_sum = sum(float(row["amount"]) for row in rows if row["amount"])  # Sums the 3rd column
    # Sums the 3rd columns i.e., include this row IF the amount field is non-empty after stripping whitespace
    total_sum = sum(float(row["amount"]) for row in rows if row["amount"].strip())
    avg_sale = total_sum / orders

    
    # Level 2 — data quality checks (loop through rows once)
    for row in rows:
        order_id = row["order_id"]

        if not row["customer"].strip():
            missing_customer.append(order_id)
        
        if not row["amount"].strip():
            missing_amount.append(order_id)

        if not row["order_date"].strip():
            missing_date.append(order_id)
        
        # negative amount — only check if amount exists first
        if row["amount"].strip() and float(row["amount"]) < 0:
            negative_amount.append(order_id)

# Print Level 1 report
print("Total Orders: ", len(rows))
print("Orders with valid amount: ", orders)
print("Total Sales: ", total_sum)
print("Average sale: ", avg_sale)

# Print Level 2 report
print("\n--- Data Quality Report ---")
print(f"Missing customer ({len(missing_customer)}): {missing_customer}")
print(f"Missing amount ({len(missing_amount)}): {missing_amount}")
print(f"Missing date ({len(missing_date)}): {missing_date}")
print(f"Negative amount ({len(negative_amount)}): {negative_amount}")
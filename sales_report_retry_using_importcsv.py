# Level 1 — write sales_report.py that:

# Opens and reads the CSV file
# Counts total number of orders
# Calculates total and average of the amount column — skipping rows where amount is missing
# Prints this report:
# Total Orders: 8
# Orders with valid amount: 7
# Total sales: 2375.24
# Average sale: 339.32
import csv

with open("sales.csv","r") as file:
    reader = csv.DictReader(file) # Earlier had used csv.reader(file)
    # header = next(reader) # Skips the header row
    rows = list(reader)

    # row_count = sum(1 for row in reader)
    orders = sum(1 for row in rows if row["amount"].strip())
    total_sum = sum(float(row["amount"]) for row in rows if row["amount"])  # Sums the 3rd column
    avg_sale = total_sum/orders
    print("Total Orders: ", len(rows) )
    print("Orders with valid amount: ",orders)
    print("Total Sales: ", total_sum)
    print("Average sale: ", avg_sale)





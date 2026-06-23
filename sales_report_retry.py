# Level 1 — write sales_report.py that:

# Opens and reads the CSV file
# Counts total number of orders
# Calculates total and average of the amount column — skipping rows where amount is missing
# Prints this report:
# Total Orders: 8
# Orders with valid amount: 7
# Total sales: 2375.24
# Average sale: 339.32

# lines = open("sales.csv").read()
# print(lines)

# total_lines = 0

# with open("sales.csv", "r") as file:
#     next(file)
#     for line in file:
#         total_lines = total_lines + 1

#  Python shortcut used to quickly count items without wasting computer memory


order_count = 0
amount_count = 0
total_sales = 0

with open("sales.csv", "r") as file:
    next(file)
    for line in file:
        # Count every row in the file
        order_count += 1
        # Split the line
        columns = line.split(",")
        # Check for column 3 (amount) is available or not
        if len(columns) > 2:
            # Strip = Return a copy of the string with leading and trailing whitespace removed.
            value = columns[2].strip()
            # Checks if value is empty or not
            if value != "":
                amount_count += 1  # Increments the count
                total_sales += float(value)  # Convert to float and get the total

print("Total Orders:", order_count)
print("Orders with valid amount: ", amount_count)
print("Total sales: ", total_sales)
average = total_sales / amount_count if amount_count > 0 else 0
print("Average sale: ", average)

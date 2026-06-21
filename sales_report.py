# Opens and reads the CSV file (use plain open() and string .split(","), or \
# Python's built-in csv module — your choice).
# Counts the total number of orders.
# Calculates the total and average of the amount column — skipping rows where amount is missing.
# Prints a small report, something like:
# Total orders: 8
# Orders with valid amount: 7
# Total sales: 2375.24
# Average sale: 339.32


lines = open("sales.csv").read().split(",")
# print(lines)

line_count = sum(1 for _ in open("sales.csv")) -1 #learning comments, as it is more data specific
# print(f"Total Orders: {line_count-1}") #learning comments - not to be done, as it is more data specific


total=0
valid_amount=0
with open("sales.csv", "r") as file: #automatically closes the file
    next(file) #skips header
    for line in file:
        columns = line.strip().split(",")
        amount_text = columns[2]
        if amount_text != "": 
            total = total + float(amount_text) #convert from str to float to avoid datatype issues
            valid_amount = valid_amount + 1

    for line in file:
        order_id = line.get("order_id","").strip()

        is_missing = not order_id

        if is_missing:
            row_count+=1  

if valid_amount>0: #divided by 0 error fix
    average_sale=total/valid_amount
else:
    average_sale=0
    
print(f"Total Orders: {line_count}")
print(f"Orders with valid amount: {valid_amount}")
print(f"Total sales: {total}")
print(f"Average sale: {average_sale}")






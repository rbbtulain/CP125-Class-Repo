import csv

def calculate_order_total(products_file, order_file, output_file):

    prices = {}

    f = open(products_file, "r", newline="")
    reader = csv.reader(f)
    next(reader) 

    for row in reader:
        product_id = row[0]
        price = float(row[2])
        prices[product_id] = price

    f.close()

    grand_total = 0

    f = open(order_file, "r", newline="")
    reader = csv.reader(f)
    next(reader)  

    output = []

    for row in reader:
        product_id = row[0]
        quantity = int(row[1])

        total_cost = prices[product_id] * quantity
        grand_total += total_cost

        output.append([product_id, f"{total_cost:.2f}"])

    f.close()


    f = open(output_file, "w", newline="")
    writer = csv.writer(f)

    writer.writerow(["product_id", "total_cost"])
    writer.writerows(output)

    f.close()

    return grand_total
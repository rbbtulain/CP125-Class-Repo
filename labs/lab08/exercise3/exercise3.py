# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv
def calculate_order_total(products_file, order_file, output_file):
    """
    Calculate total cost for each product in order.

    Args:
        products_file: path to products CSV (product_id,product_name,price)
        order_file: path to order CSV (product_id,quantity)
        output_file: path to output CSV file

    Returns:
        float: grand total of all orders
    """
    products = open(products_file, "r", newline = "")
    order = open(order_file, "r", newline = "")

    reader = csv.reader(products)
    reader = csv.reader(order)

    for item in order:
        

    products.close()
    order.close()

    total = open(output_file, "w")
    writer = csv.writer(total)

    total.close()

# Test your code here
result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", "labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")

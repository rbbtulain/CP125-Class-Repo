# Lab 08 Exercise 5: Sales Summary
# Write your code below:

def summarize_sales(input_file, output_file):
    """
    Calculate sales statistics: total, average, highest, and lowest revenue.

    Args:
        input_file: path to sales CSV (product,quantity,price)
        output_file: path to output text file

    Returns:
        tuple: (total, average, highest, lowest)
    """
    # TODO: Implement this function
    import csv

def summarize_sales(input_file, output_file):

    revenues = []

    f = open(input_file, "r", newline="")
    reader = csv.reader(f)
    next(reader)  # skip header

    for row in reader:
        quantity = int(row[1])
        price = float(row[2])

        revenue = quantity * price
        revenues.append(revenue)

    f.close()

    total = sum(revenues)
    average = total / len(revenues)
    highest = max(revenues)
    lowest = min(revenues)

    # Write summary
    f = open(output_file, "w")

    f.write(f"Total Revenue: ${total:.2f}\n")
    f.write(f"Average Revenue: ${average:.2f}\n")
    f.write(f"Highest Revenue: ${highest:.2f}\n")
    f.write(f"Lowest Revenue: ${lowest:.2f}\n")

    f.close()

    return (total, average, highest, lowest)


# Test your code here
result = summarize_sales("data/sales.csv", "data/summary.txt")
print(f"Total: ${result[0]:.2f}, Avg: ${result[1]:.2f}, High: ${result[2]:.2f}, Low: ${result[3]:.2f}")

# Programmer Name: ______________________
# Program Description:
# This program accepts 5 integer values from the user,
# stores them in a list, displays the numbers in ascending order,
# calculates the sum, and finds the largest number.

def process_numbers():
    numbers = []

    # Read 5 integer inputs from user
    for i in range(5):
        num = int(input(f"Enter integer {i + 1}: "))
        numbers.append(num)

    # Sort numbers in ascending order
    ascending_numbers = sorted(numbers)

    # Calculate sum
    total_sum = sum(numbers)

    # Find largest number
    largest_number = max(numbers)

    # Display output
    print("\nNumbers in ascending order:", ascending_numbers)
    print("Sum of all numbers:", total_sum)
    print("Largest number:", largest_number)


# Call the function
process_numbers()

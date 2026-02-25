# Programmer Name: NURUL ROBBIATUL AIN BINTI ABDULLAH
# Program Description:
# A program that accepts 5 integer input values from the user and is stored in a list. 
# The program will perform the following task: 
    # 1. Print all the numbers that has been entered in ascending order 
    # 2. Calculate and find the sum of all the entered numbers 
    # 3. Find and print the largest number

def process_numbers():
    numbers = []
    for i in range(5):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    ascending_numbers = sorted(numbers)
    total_sum = sum(numbers)
    largest_number = max(numbers)

    print("Numbers in ascending order:", ascending_numbers)
    print("Sum of all numbers:", total_sum)
    print("Largest number:", largest_number)
    print("\n=== Code Execution Successful ===")

process_numbers()
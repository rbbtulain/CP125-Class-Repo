#Name: CHENG KARMEN
#Problem description: Create a program that accepts 5 integer input values from the user and is stored in a list.

def numbers_list():
    numbers = []

    for i in range(1, 6):
        number = int(input(f"Enter number {i}: "))
        numbers.append(number)

    print(f"Numbers in ascending order: {sorted(numbers)}")
    print(f"Sum of all numbers: {sum(numbers)}")
    print(f"Largest number: {max(numbers)}")

numbers_list()

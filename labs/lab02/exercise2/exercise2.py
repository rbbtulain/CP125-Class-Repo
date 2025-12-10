# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    # TODO: Implement this function
    # Calculate total cost for tents and meals
    total_tent = math.ceil(participants / tent_capacity) * tent_price

    total_price = ((total_tent)) + (meal_price * participants)
    return total_price

# Test your code here
print("Testing Camping Logistics...")


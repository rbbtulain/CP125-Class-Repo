# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):

    round_trip_km = one_way_km * 2
    cost = (round_trip_km / km_per_liter) * price_per_liter
    if budget >= cost:
        budget = True
    else:
        budget = False
    return budget

# Test your code here

print("Testing Road Trip Budgeter...")
result = is_budget_sufficient(5, 2, 0.70, 100)

if result:
    print("Your money is enough for a round trip")
else:
    print("Your money is not enough fo a round trip")

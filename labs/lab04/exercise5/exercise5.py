

def find_momentum_days(prices):
    
    
    for i in range(1, len (prices) - 1):
        if prices[i] > prices[i - 1] and prices[i] > prices[i + 1]:
            yield i




# Test
prices = [100, 102, 105, 107, 106, 108, 112, 114]
result = find_momentum_days(prices)
print(f"Momentum days: {result}")  # Expected: [2, 5, 6]


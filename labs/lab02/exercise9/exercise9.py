def calculate_level(xp):
    level = 1
    cost = 100

    while xp >= cost:
        xp -= cost
        level += 1
        cost += 100

    return level, xp
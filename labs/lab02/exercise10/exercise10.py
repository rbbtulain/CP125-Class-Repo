def calculate_battery_usage(distance, sport_mode):
    battery_per_10m = 1.5

    if sport_mode:
        battery_per_10m = battery_per_10m * 1.5

    battery_used = (distance / 10) * battery_per_10m
    return battery_used


def can_complete_trip(distance, battery_level, sport_mode):
    round_trip_distance = distance * 2

    required_battery = calculate_battery_usage(round_trip_distance, sport_mode)

    if battery_level >= required_battery:
        return True
    else:
        return False


# Example
result = can_complete_trip(200, 80, True)
print(result)
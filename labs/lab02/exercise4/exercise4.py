def get_hourly_rate(vehicle_type, hour_24):
    # Validate hour
    if hour_24 < 0 or hour_24 > 23:
        raise ValueError("hour_24 must be between 0 and 23")

    # Electric vehicles: RM2.00 always
    if vehicle_type == "Electric":
        return 2.00

    # Hybrid vehicles
    if vehicle_type == "Hybrid":
        # Night rate: 22–23 OR 0–6
        if hour_24 >= 22 or hour_24 <= 6:
            return 2.00
        else:
            return 5.00

    # All other vehicles: RM5.00 always
    return 5.00


# Test your code
print("Testing Dynamic Parking Rate...")
print(get_hourly_rate("Electric", 14))  # 2.0
print(get_hourly_rate("Hybrid", 23))    # 2.0
print(get_hourly_rate("Hybrid", 10))    # 5.0
print(get_hourly_rate("Other", 8))      # 5.0

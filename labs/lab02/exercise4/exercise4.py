def get_hourly_rate(vehicle_type, hour_24):

    if hour_24 < 0 or hour_24 > 23:
        raise ValueError("hour_24 must be between 0 and 23")


    if vehicle_type == "Electric":
        return 2.00


    if vehicle_type == "Hybrid":
        
        if hour_24 >= 22 or hour_24 <= 6:
            return 2.00
        else:
            return 5.00


    return 5.00


# Test your code
print("Testing Dynamic Parking Rate...")
print(get_hourly_rate("Electric", 14))  
print(get_hourly_rate("Hybrid", 23))   
print(get_hourly_rate("Hybrid", 10))    
print(get_hourly_rate("Other", 8))     

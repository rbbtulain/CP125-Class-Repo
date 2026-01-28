
def filter_query_times(times):
    """
    Remove slow outliers (mean + std deviation) and return sorted times.
    """
   
    
    mean_time = sum(times) / len(times)
    variance = sum((x - mean_time) ** 2 for x in times) / len(times)
    std_deviation = variance ** 0.5
    threshold = mean_time + std_deviation
    
    filtered_times = [t for t in times if t <= threshold]
    return sorted(filtered_times)


# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]

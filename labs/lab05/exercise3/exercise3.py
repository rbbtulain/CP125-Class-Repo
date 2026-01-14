
def find_bottleneck_index(traceroute):
    """
    Find the index of the hop where the largest latency jump begins.
    """
    if len(traceroute) < 2:
        return -1
    largest_jump = 0
    bottleneck_index = -1
    for i in range(1, len(traceroute)):
        previous_latency = traceroute[i - 1][1]
        current_latency = traceroute[i][1]
        jump = current_latency - previous_latency
        if jump > largest_jump:
            largest_jump = jump
            bottleneck_index = i - 1
    return bottleneck_index

# Test
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1

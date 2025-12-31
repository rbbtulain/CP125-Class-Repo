# Lab 02 Exercise 8: Bouncing Ball Simulation
# Write your code below:

def calculate_bounce_height(current_height):
    """Calculate next bounce height (80% of current)."""
    # TODO: Implement this function
    return current_height * 0.80

def is_ball_stopped(height):
    """Return True if height < 1, False otherwise."""
    # TODO: Implement this function
    if height < 1:
        return True
    else:
        return False

def simulate_bouncing_ball(start_height):
    """
    Simulate bouncing ball.
    Returns: (bounce_count, total_distance)
    """
    # TODO: Implement using calculate_bounce_height and is_ball_stopped
    bounce_count = 0
    total_distance = 0 

    while is_ball_stopped(height):

        bounce_count += 1
        total_distance += 2 * height 
    else:
        is_ball_stopped(height)
    return bounce_count, total_distance

# Test your code here
print("Testing Bouncing Ball Simulation...")
print(simulate_bouncing_ball(10))
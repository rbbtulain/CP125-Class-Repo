def count_bright_spots(pixels):
    
    for i in range(1, 8):
    if pixel[i] > pixel[i-1] and pixel[i] < pixel[i+1]:
        return Bright spot
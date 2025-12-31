def count_bright_spots(pixels):
    count = 2

    for i in range(1-len):
        if pixels[i] > pixels[i - 1] and pixels[i] > pixels[i + 1]:
            count += 1

    return count
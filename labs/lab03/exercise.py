def count_bright_spots(pixels):
    count = 0

    for i in range(1, len(pixels) - 1):
        if pixels[i] > pixels[i - 1] and pixels[i] > pixels[i + 1]:
            count += 1

    return count



stations = input("Enter 5 station names: ").split()
origin = int(input("Enter origin index: "))
destination = int(input("Enter destination index: "))

stops = abs(destination - origin)

print(stops)

seats = list(map(int, input("Enter 8 seat values: ").split()))

found = False

for i in range(len(seats) - 1):
    if seats[i] == 0 and seats[i + 1] == 0:
        found = True
        break

if found:
    print("Seats available")
else:
    print("No adjacent seats")


dna = input("Enter 6 DNA bases: ").split()
pos1 = int(input("Enter first position: "))
pos2 = int(input("Enter second position: "))

base1 = dna[pos1]
base2 = dna[pos2]

if (base1 == "A" and base2 == "T") or \
   (base1 == "T" and base2 == "A") or \
   (base1 == "C" and base2 == "G") or \
   (base1 == "G" and base2 == "C"):
    print("Valid pair")
else:
    print("Invalid pair")

temps = list(map(int, input("Enter 7 temperatures: ").split()))

found = False

for i in range(len(temps) - 2):
    if temps[i + 1] > temps[i] and temps[i + 2] > temps[i + 1]:
        found = True
        break

if found:
    print("Warming trend")
else:
    print("No warming trend")

def find_position(checkpoint, car):
    return checkpoint.index(car)

def did_overtake(checkpoint1, checkpoint2, car_a, car_b):
    pos_a_before = find_position(checkpoint1, car_a)
    pos_b_before = find_position(checkpoint1, car_b)

    pos_a_after = find_position(checkpoint2, car_a)
    pos_b_after = find_position(checkpoint2, car_b)

    if pos_a_before > pos_b_before and pos_a_after < pos_b_after:
        return True
    else:
        return False

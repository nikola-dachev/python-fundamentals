tank_capacity = 255
number_of_lines = int(input())
sum = 0

for _ in range (number_of_lines):
    poured_water = int(input())

    if poured_water <= tank_capacity:
        tank_capacity -= poured_water
        sum +=poured_water

    else:
        print("Insufficient capacity!")
        continue

print(sum)


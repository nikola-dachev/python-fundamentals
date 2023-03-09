number_of_lines = int(input())
capacity = 255
total_litres = 0

for i in range(number_of_lines):
    liters_of_water = int(input())

    if liters_of_water > capacity:
        print(f'Insufficient capacity!')
        continue

    capacity -= liters_of_water
    total_litres += liters_of_water

print(total_litres)

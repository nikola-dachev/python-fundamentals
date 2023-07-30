my_dict = {}
number_of_cars = int(input())

for _ in range(number_of_cars):
    car,mileage,fuel = input().split('|')
    mileage = int(mileage)
    fuel = int(fuel)
    my_dict[car] = {'mileage': mileage, 'fuel': fuel}

while True:
    command = input()

    if command == 'Stop':
        break

    current_command = command.split(' : ')
    action = current_command[0]

    if action == 'Drive':
        car = current_command[1]
        distance = int(current_command[2])
        fuel = int(current_command[3])

        if my_dict[car]['fuel'] >= fuel:
            my_dict[car]['fuel'] -=fuel
            my_dict[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        else:
            print("Not enough fuel to make that ride")

        if my_dict[car]['mileage'] >= 100000:
            del my_dict[car]
            print(f"Time to sell the {car}!")

    elif action == 'Refuel':
        car = current_command[1]
        fuel = int(current_command[2])
        current_fuel = my_dict[car]['fuel']

        my_dict[car]['fuel'] += fuel

        if my_dict[car]['fuel'] > 75:
            my_dict[car]['fuel'] = 75

        print(f"{car} refueled with {my_dict[car]['fuel'] - current_fuel} liters")

    elif action == 'Revert':
        car = current_command[1]
        kilometers = int(current_command[2])

        my_dict[car]['mileage'] -= kilometers

        if my_dict[car]['mileage'] < 10000:
            my_dict[car]['mileage'] = 10000

        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car , value in my_dict.items():
    print(f"{car} -> Mileage: {my_dict[car]['mileage']} kms, Fuel in the tank: {my_dict[car]['fuel']} lt.")


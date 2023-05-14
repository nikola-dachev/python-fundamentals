number_of_cars = int(input())
my_dict = {}

for index in range(number_of_cars):
    car_command = input().split('|')
    car = car_command[0]
    mileage = int(car_command[1])
    fuel = int(car_command[2])
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

        if my_dict[car]['fuel'] < fuel:
            print("Not enough fuel to make that ride")

        else:
            my_dict[car]['mileage'] += distance
            my_dict[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if my_dict[car]['mileage'] >= 100000:
            print(f"Time to sell the {car}!")
            del my_dict[car]

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
        print(f"{car} mileage decreased by {kilometers} kilometers")
        if my_dict[car]['mileage'] < 10000:
            my_dict[car]['mileage'] = 10000

for car, value in my_dict.items():
    print(f"{car} -> Mileage: {my_dict[car]['mileage']} kms, Fuel in the tank: {my_dict[car]['fuel']} lt.")

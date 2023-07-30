my_dict = {}

while True:
    command = input()

    if command == 'Sail':
        break

    current_command = command.split('||')
    city = current_command[0]
    population = int(current_command[1])
    gold = int(current_command[2])

    if city not in my_dict:
        my_dict[city] = {'population': population, 'gold': gold}
    else:
        my_dict[city]['population'] += population
        my_dict[city]['gold'] += gold

while True:
    new_command = input()

    if new_command == 'End':
        break

    current_command_new = new_command.split('=>')
    action = current_command_new[0]

    if action == 'Plunder':
        city = current_command_new[1]
        population = int(current_command_new[2])
        gold = int(current_command_new[3])

        my_dict[city]['population'] -= population
        my_dict[city]['gold'] -= gold

        print(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")

        if my_dict[city]['population'] <= 0 or my_dict[city]['gold'] <= 0:
            print(f"{city} has been wiped off the map!")
            del my_dict[city]

    elif action == 'Prosper':
        city = current_command_new[1]
        gold = int(current_command_new[2])

        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue

        my_dict[city]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {city} now has {my_dict[city]['gold']} gold.")

if len(my_dict) > 0:
    print(f"Ahoy, Captain! There are {len(my_dict)} wealthy settlements to go to:")

    for city, value in my_dict.items():
        print(f"{city} -> Population: {my_dict[city]['population']} citizens, Gold: {my_dict[city]['gold']} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

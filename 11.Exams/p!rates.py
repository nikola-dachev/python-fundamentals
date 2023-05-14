my_dict={}
while True:
    command = input()

    if command =='Sail':
        break
    current_command = command.split('||')
    city = current_command[0]
    population = int(current_command[1])
    gold = int(current_command[2])

    if city not in my_dict:
       my_dict[city]= {'population': population, 'gold': gold}

    else:
        my_dict[city]['population']+=population
        my_dict[city]['gold'] += gold


while True:
    command_1 = input()

    if command_1 =='End':
        break

    current_command_1= command_1.split('=>')
    action = current_command_1[0]

    if action == 'Plunder':
        city = current_command_1[1]
        population = int(current_command_1[2])
        gold = int(current_command_1[3])
        my_dict[city]['population']-= population
        my_dict[city]['gold'] -= gold
        print(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")

        if my_dict[city]['population'] <=0 or my_dict[city]['gold']<=0:
            print(f"{city} has been wiped off the map!")
            del my_dict[city]

    elif action == 'Prosper':
        city = current_command_1[1]
        gold = int(current_command_1[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        else:
            my_dict[city]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {my_dict[city]['gold']} gold.")


if len(my_dict)== 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

else:
    print(f"Ahoy, Captain! There are {len(my_dict)} wealthy settlements to go to:")
    for city, value in my_dict.items():
        print(f"{city} -> Population: {my_dict[city]['population']} citizens, Gold: {my_dict[city]['gold']} kg")

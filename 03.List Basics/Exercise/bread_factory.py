coins = 100
energy = 100
events = input().split('|')

for event in events:
    one_event = event.split('-')
    type_of_event = one_event[0]
    value_of_event = int(one_event[1])

    if type_of_event =='rest':
        current_energy = energy
        energy += value_of_event
        if energy >100:
            energy = 100
        print(f'You gained {energy - current_energy} energy.')
        print(f'Current energy: {energy}.')


    elif type_of_event =='order':
        if energy >=30:
            energy -=30
            coins += value_of_event
            print(f'You earned {value_of_event} coins.')
        else:
            energy += 50
            print(f'You had to rest!')

    else:
        if coins >= value_of_event:
            coins -=value_of_event
            print(f'You bought {type_of_event}.')
        else:
            print(f'Closed! Cannot afford {type_of_event}.')
            break

else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")



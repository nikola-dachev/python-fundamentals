status_pirate_ship = [int(x) for x in input().split('>')]
status_war_ship = [int(x) for x in input().split('>')]
max_health_capacity = int(input())


while True:
    command = input()
    if command == "Retire":
        print(f"Pirate ship status: {sum(status_pirate_ship)}")
        print(f"Warship status: {sum(status_war_ship)}")
        break

    current_command = command.split()
    action = current_command[0]

    if action == 'Fire':
        index = int(current_command[1])
        damage = int(current_command[2])
        if 0<= index < len(status_war_ship):
            status_war_ship[index] = status_war_ship[index] - damage
            if status_war_ship[index] < 0:
                print(f"You won! The enemy ship has sunken.")
                exit(0)

        else:
            continue

    elif action == 'Defend':
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        damage_1 = int(current_command[3])

        if 0<=start_index <len(status_pirate_ship) and 0<=end_index <len(status_pirate_ship):
            for ind in range(start_index,end_index +1):
                status_pirate_ship[ind] = status_pirate_ship[ind] - damage_1
                if status_pirate_ship[ind]<0:
                    print(f"You lost! The pirate ship has sunken.")
                    exit(0)

        else:
            continue

    elif action == 'Repair':
        index = int(current_command[1])
        health = int(current_command[2])

        if 0<= index < len(status_pirate_ship):
            status_pirate_ship[index] = status_pirate_ship[index] + health
            if status_pirate_ship[index] > max_health_capacity:
                status_pirate_ship[index] = max_health_capacity
        else:
            continue

    elif action == 'Status':
        count_repair = 0.2 * max_health_capacity
        sections_for_repair = 0
        for section in status_pirate_ship:
            if section < count_repair:
                sections_for_repair +=1
        print(f"{sections_for_repair} sections need repair.")

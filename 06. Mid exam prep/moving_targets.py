targets_list = [int(el) for el in input().split()]

while True:
    command = input()

    if command == 'End':
        break
    current_command = command.split()
    action = current_command[0]

    if action == 'Shoot':
        index = int(current_command[1])
        power = int(current_command[2])

        if 0 <= index < len(targets_list):
            targets_list[index] -= power
            if targets_list[index] <= 0:
                targets_list.pop(index)

    elif action == 'Add':
        index = int(current_command[1])
        value = int(current_command[2])

        if 0 <= index < len(targets_list):
            targets_list.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == 'Strike':
        index = int(current_command[1])
        radius = int(current_command[2])

        if 0 <= index < len(targets_list) and 0 <= index + radius < len(targets_list) and 0 <= index - radius < len(
                targets_list):
            del targets_list[index:index + radius]
            del targets_list[index - radius: index + 1]

        else:
            print("Strike missed!")

print(*targets_list, sep='|')

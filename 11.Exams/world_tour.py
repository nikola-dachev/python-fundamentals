destinations = input()

while True:
    command = input()

    if command == 'Travel':
        break

    current_command = command.split(':')
    action = current_command[0]

    if action == 'Add Stop':
        index = int(current_command[1])
        string = current_command[2]

        if 0 <= index < len(destinations):
            destinations = destinations[:index] + string + destinations[index:]

    elif action == 'Remove Stop':
        start_index = int(current_command[1])
        end_index = int(current_command[2])

        if 0 <= start_index < len(destinations) and 0 <= end_index < len(destinations):
            destinations = destinations[:start_index] + destinations[end_index + 1:]

    elif action == 'Switch':
        old_string = current_command[1]
        new_string = current_command[2]

        if old_string in destinations:
            destinations = destinations.replace(old_string, new_string)

    print(destinations)

print(f"Ready for world tour! Planned stops: {destinations}")


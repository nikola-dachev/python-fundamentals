message = input()
asci_sum = 0

while True:
    command = input()

    if command == 'Finish':
        break

    current_command = command.split()
    action = current_command[0]

    if action == 'Replace':
        current_char = current_command[1]
        new_char = current_command[2]

        message = message.replace(current_char, new_char)
        print(message)

    elif action == 'Cut':
        start_index = int(current_command[1])
        end_index = int(current_command[2])

        if 0 <= start_index < len(message) and 0 <= end_index < len(message):
            message = message[:start_index] + message[end_index +1:]
            print(message)

        else:
            print("Invalid indices!")

    elif action == 'Make':
        upper_lower_command = current_command[1]

        if upper_lower_command == 'Upper':
            message = message.upper()

        elif upper_lower_command == 'Lower':
            message = message.lower()

        print(message)

    elif action == 'Check':
        string = current_command[1]

        if string in message:
            print(f"Message contains {string}")

        else:
            print(f"Message doesn't contain {string}")

    elif action == 'Sum':
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        new_substring = ''

        if 0 <= start_index < len(message) and 0 <= end_index < len(message):
            new_substring = message[start_index:end_index +1]
            for char in new_substring:
                asci_sum += ord(char)
            print(asci_sum)

        else:
            print("Invalid indices!")
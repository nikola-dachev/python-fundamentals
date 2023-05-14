message = input()

while True:
    command = input()

    if command == "Reveal":
        print(f"You have a new text message: {message}")
        break

    current_command = command.split(":|:")
    action = current_command[0]

    if action == 'InsertSpace':
        index = int(current_command[1])
        message = message[:index] + ' ' + message[index:]
        print(f'{message}')

    elif action == 'Reverse':
        substring = current_command[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            reversed_substring = substring[::-1]
            message += reversed_substring
            print(f'{message}')

        else:
            print('error')

    elif action == 'ChangeAll':
        substring = current_command[1]
        replacement_string = current_command[2]
        message = message.replace(substring, replacement_string)
        print(f'{message}')

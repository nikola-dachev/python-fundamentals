
my_list = []

while True:
    command = input()

    if command == 'end':
        break

    current_command = command.split()
    action = current_command[0]

    if action == 'Chat':
        message = current_command[1]
        my_list.append(message)

    elif action == 'Delete':
        message = current_command[1]
        if message in my_list:
            my_list.remove(message)

    elif action == 'Edit':
        message = current_command[1]
        edited_message = current_command[2]
        if message in my_list:
            index = my_list.index(message)
            my_list[index] = edited_message

    elif action == 'Pin':
        message = current_command[1]
        if message in my_list:
            my_list.append(message)
            my_list.remove(message)

    elif action == 'Spam':
        messages = current_command[1:]
        for el in messages:
            my_list.append(el)

print('\n'.join(my_list))
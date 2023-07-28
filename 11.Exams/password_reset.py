user_password = input()

while True:
    command = input()

    if command == 'Done':
        break

    if command == 'TakeOdd':
        new_password = ''
        for index in range(len(user_password)):
            if index % 2 != 0:
                new_password += user_password[index]
        user_password = new_password
        print(new_password)

    current_command = command.split()
    action = current_command[0]

    if action == 'Cut':
        index = int(current_command[1])
        length = int(current_command[2])
        user_password = user_password[:index] + user_password[index + length:]

        print(user_password)

    elif action == 'Substitute':
        substring = current_command[1]
        substitute = current_command[2]

        if substring in user_password:
            user_password = user_password.replace(substring, substitute)
            print(user_password)

        else:
            print("Nothing to replace!")

print(f"Your password is: {user_password}")
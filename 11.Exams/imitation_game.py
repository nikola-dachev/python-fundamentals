encrypted_message = input()

while True:

    command = input()
    if command == 'Decode':
        print(f'The decrypted message is: {encrypted_message}')
        break
    current_command = command.split('|')
    action = current_command[0]

    if action == 'Move':
        number_of_letters =int(current_command[1])
        for _ in range(number_of_letters):
            encrypted_message = encrypted_message[1:]+encrypted_message[0]


    elif action == 'Insert':
        current_index = int(current_command[1])
        value = current_command[2]
        encrypted_message = encrypted_message[:current_index] + value + encrypted_message[current_index:]

    elif action =='ChangeAll':
        current_substring= current_command[1]
        replacement = current_command[2]
        encrypted_message = encrypted_message.replace(current_substring, replacement)
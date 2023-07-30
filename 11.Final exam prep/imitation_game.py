encrypted_text = input()

while True:
    command = input()

    if command == 'Decode':
        break

    current_command = command.split('|')

    action = current_command[0]

    if action == 'Move':
        number_of_letters = int(current_command[1])
        encrypted_text = encrypted_text[number_of_letters:] + encrypted_text[:number_of_letters]

    elif action == 'Insert':
        index = int(current_command[1])
        value = current_command[2]

        encrypted_text = encrypted_text[:index] + value + encrypted_text[index:]

    elif action == 'ChangeAll':
        substring = current_command[1]
        replacement = current_command[2]

        encrypted_text = encrypted_text.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_text}")


my_dict = {}
while True:
    command = input()

    if command == 'stop':
        break

    second_command = int(input())

    if command not in my_dict:
        my_dict[command] = second_command

    else:
        my_dict[command] += second_command

for key, value in my_dict.items():
    print(f"{key} -> {value}")


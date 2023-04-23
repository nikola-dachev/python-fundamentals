my_dict = {}
while True:
    command = input()
    if '-' not in command:
        break
    current_command = command.split('-')
    person = current_command[0]
    number = current_command[1]
    my_dict[person] = number

for i in range(int(command)):
    searched_person = input()

    if searched_person in my_dict.keys():
        print(f"{searched_person} -> {my_dict[searched_person]}")
    else:
        print(f"Contact {searched_person} does not exist.")

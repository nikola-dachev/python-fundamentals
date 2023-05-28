gifts_name = input().split()

while True:
    command = input()

    if command == 'No Money':
        break

    current_command = command.split()
    action = current_command[0]
    gift = current_command[1]

    if action == 'OutOfStock':
        for index in range(len(gifts_name)):
            if gift in gifts_name[index]:
                gifts_name[index] = 'None'

    elif action == 'Required':
        index = int(current_command[2])
        if 0<= index < len(gifts_name):
            gifts_name[index] = gift

    elif action == 'JustInCase':
        gifts_name[-1] = gift

for item in gifts_name:
    if item !='None':
        print(item, end = ' ')
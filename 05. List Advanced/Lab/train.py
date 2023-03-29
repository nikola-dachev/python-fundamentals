wagons = int(input())

train=[0]* wagons

while True:
    command = input()
    if command =='End':
        print(train)
        break
    current_command = command.split()
    action = current_command[0]

    if action =='add':
        train[-1] += int(current_command[1])
    elif action =='insert':
        train[int(current_command[1])]+= int(current_command[2])
    elif action == 'leave':
        train[int(current_command[1])] -= int(current_command[2])




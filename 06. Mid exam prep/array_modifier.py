numbers = [int(el) for el in input().split()]

while True:
    command = input()
    if command =='end':
        break

    current_commmand = command.split()
    action = current_commmand[0]

    if action == 'swap':
        index_1 = int(current_commmand[1])
        index_2 = int(current_commmand[2])
        numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]

    elif action == 'multiply':
        index_1 = int(current_commmand[1])
        index_2 = int(current_commmand[2])
        numbers[index_1] = numbers[index_1] * numbers[index_2]

    elif action == 'decrease':
        for index in range(len(numbers)):
            numbers[index] -=1

print(*numbers, sep = ', ')
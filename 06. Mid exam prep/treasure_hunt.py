from collections import deque

treasury_chest = deque(input().split('|'))

while True:
    command = input()
    if command == 'Yohoho!':
        break
    current_command = command.split()
    action = current_command[0]

    if action == 'Loot':
        for item in current_command[1:]:
            if item not in treasury_chest:
                treasury_chest.appendleft(item)

    elif action == 'Drop':
        index = int(current_command[1])
        if 0 <= index < len(treasury_chest):
            treasury_chest.append(treasury_chest[index])
            del treasury_chest[index]


    elif action == 'Steal':
        stolen_items_list = deque()
        stolen_items = int(current_command[1])

        if 0 <= stolen_items < len(treasury_chest):
            for time_ in range(stolen_items):
                stolen_items_list.appendleft(treasury_chest.pop())
            print(*stolen_items_list, sep=', ')

        else:
            for time_ in range(len(treasury_chest)):
                stolen_items_list.appendleft(treasury_chest.pop())
            print(*stolen_items_list, sep=', ')

if treasury_chest:
    total_gain = 0
    for el in treasury_chest:
        total_gain += len(el)
    average_gain = total_gain / len(treasury_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")

else:
    print("Failed treasure hunt.")


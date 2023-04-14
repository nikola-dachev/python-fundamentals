initial_list = input().split('!')
final_list = initial_list

while True:
    command = input()
    if command =="Go Shopping!":
        print(', '.join(final_list))
        break
    current_command = command.split()
    action = current_command[0]
    item = current_command[1]

    if action == 'Urgent':
        if item in final_list:
            continue
        else:
            final_list.insert(0,item)

    elif action == 'Unnecessary':
        if item not in final_list:
            continue
        else:
            final_list.remove(item)

    elif action =='Correct':
        new_item = current_command[2]
        if item not in final_list:
            continue
        else:
            final_list = list(map(lambda x: x.replace(item, new_item), final_list))
    elif action == 'Rearrange':
        if item not in final_list:
            continue
        else:
            final_list.remove(item)
            final_list.append(item)


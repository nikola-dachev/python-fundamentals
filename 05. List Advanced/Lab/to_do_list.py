
to_do_list = [0] * 10
while True:
    command = input()
    if command =='End':
        final_list =[element for element in to_do_list if element!=0]
        print(final_list)
        break

    current_command = command.split('-')
    importance = int(current_command[0])
    index = importance - 1
    note = current_command[1]
    to_do_list[index]= note


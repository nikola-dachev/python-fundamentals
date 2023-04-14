my_list= input().split()
number_of_moves = 0

while True:
    command = input()
    if command == 'end':
        if len(my_list) > 0:
            print(f"Sorry you lose :(")
            print(' '.join(my_list))
        break

    current_command = command.split()
    first_index = int(current_command[0])
    second_index = int(current_command[1])

    number_of_moves +=1

    if first_index > len(my_list)  or second_index > len(my_list) or first_index==second_index or first_index<0 or second_index <0:
        mid_point = len(my_list)//2
        element_to_add = f'-{number_of_moves}a'
        my_list = my_list[0:mid_point] + [element_to_add] + my_list[mid_point:]
        my_list = my_list[0:mid_point] + [element_to_add] + my_list[mid_point:]
        print(f"Invalid input! Adding additional elements to the board")

    else:
        if my_list[first_index]== my_list[second_index]:
            el = my_list[first_index]
            my_list.pop(first_index)
            my_list.remove(el)
            print(f"Congrats! You have found matching elements - {el}!")

        else:
            print(f"Try again!")

    if len(my_list)==0:
        print(f"You have won in {number_of_moves} turns!")
        break



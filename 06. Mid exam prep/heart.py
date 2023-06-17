neighbourhood_list = [int(el) for el in input().split('@')]
current_cupid_position = 0

while True:
    command = input()
    if command == 'Love!':
        break
    current_command = command.split()
    jump_lenght_index = int(current_command[1])

    if 0 <= jump_lenght_index + current_cupid_position < len(neighbourhood_list):
        if neighbourhood_list[jump_lenght_index+ current_cupid_position] <= 0:
            print(f"Place {jump_lenght_index+ current_cupid_position} already had Valentine's day.")
        else:
            neighbourhood_list[jump_lenght_index+current_cupid_position] -= 2
            current_cupid_position += jump_lenght_index
    else:
        current_cupid_position = 0
        neighbourhood_list[0] -= 2
        if neighbourhood_list[current_cupid_position] <= 0:
            print(f"Place {current_cupid_position} already had Valentine's day.")

    if neighbourhood_list[current_cupid_position] == 0:
        print(f"Place {current_cupid_position} has Valentine's day.")

print(f"Cupid's last position was {current_cupid_position}.")

if sum(neighbourhood_list) <= 0:
    print("Mission was successful.")

else:
    failed_count = 0
    for index in range(len(neighbourhood_list)):
        if neighbourhood_list[index] >0:
            failed_count +=1
    print(f"Cupid has failed {failed_count} places.")


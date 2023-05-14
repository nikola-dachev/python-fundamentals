number_of_pieces = int(input())
my_dict = {}

for index in range(number_of_pieces):
    piece_command = input().split('|')
    piece = piece_command[0]
    composer = piece_command[1]
    key = piece_command[2]
    my_dict[piece] = {'composer': composer, 'key': key}

while True:
    command = input()

    if command == 'Stop':
        break

    current_command = command.split('|')
    action = current_command[0]

    if action == 'Add':
        piece = current_command[1]
        composer = current_command[2]
        key = current_command[3]

        if piece in my_dict:
            print(f"{piece} is already in the collection!")

        else:
            my_dict[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == 'Remove':
        piece = current_command[1]

        if piece not in my_dict:
            print(f"Invalid operation! {piece} does not exist in the collection.")

        else:
            print(f"Successfully removed {piece}!")
            del my_dict[piece]



    elif action == 'ChangeKey':
        piece = current_command[1]
        new_key = current_command[2]

        if piece not in my_dict:
            print(f"Invalid operation! {piece} does not exist in the collection.")

        else:
            my_dict[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")

for piece, value in my_dict.items():
    print(f"{piece} -> Composer: {my_dict[piece]['composer']}, Key: {my_dict[piece]['key']}")

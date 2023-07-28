n = int(input())

my_dict = {}

for _ in range(n):
  piece, composer, key = input().split('|')
  my_dict[piece] = [composer, key]

while True:
  command = input()

  if command =='Stop':
    break

  current_command = command.split('|')
  action = current_command[0]

  if action == 'Add':
    piece = current_command[1]
    composer = current_command[2]
    key = current_command[3]

    if piece not in my_dict:
      my_dict[piece] = []
      my_dict[piece].append(composer)
      my_dict[piece].append(key)
      print(f"{piece} by {composer} in {key} added to the collection!")

    else:
      print(f"{piece} is already in the collection!")

  elif action == 'Remove':
    piece = current_command[1]

    if piece in my_dict:
      del my_dict[piece]
      print(f"Successfully removed {piece}!")

    else:
      print(f"Invalid operation! {piece} does not exist in the collection.")

  elif action == 'ChangeKey':
    piece = current_command[1]
    new_key = current_command[2]

    if piece in my_dict:
      my_dict[piece][1] = new_key
      print(f"Changed the key of {piece} to {new_key}!")

    else:
      print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, value in my_dict.items():
  print(f"{piece} -> Composer: {my_dict[piece][0]}, Key: {my_dict[piece][1]}")


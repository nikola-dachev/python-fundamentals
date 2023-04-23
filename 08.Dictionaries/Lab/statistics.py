my_dict = {}

while True:
  command = input()
  if command == 'statistics':
    print(f"Products in stock:")
    for key, value in my_dict.items():
      print(f"- {key}: {value}")
    print(f"Total Products: {len(my_dict)}")
    print(f"Total Quantity: {sum(my_dict.values())}")
    break

  current_command = command.split(': ')
  product = current_command[0]
  quantity = int(current_command[1])

  if product not in my_dict:
    my_dict[product] = quantity

  else:
    my_dict[product] += quantity

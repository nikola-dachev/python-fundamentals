my_dict = {}

while True:
    command = input()
    if command == 'buy':
        break

    current_command = command.split()
    name = current_command[0]
    price = float(current_command[1])
    quantity = int(current_command[2])

    if name not in my_dict:
        my_dict[name] = []
        my_dict[name].append(price)
        my_dict[name].append(quantity)
    else:
        my_dict[name][0] = price
        my_dict[name][1] +=quantity

for key , value in my_dict.items():
    total_price = 1
    for el in value:
        total_price *= el
    print(f'{key} -> {total_price:.2f}')
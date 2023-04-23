my_dict = {}
my_dict_2 = {}
while True:
    command = input()
    if command == 'buy':
        break

    current_command = command.split()

    product = current_command[0]
    price = float(current_command[1])
    quantity = int(current_command[2])

    if product not in my_dict:
        my_dict[product] = price
        my_dict_2[product] = quantity

    else:
        my_dict[product] = price
        my_dict_2[product] += quantity

for product in my_dict:
    price = my_dict[product]
    quantity = my_dict_2[product]
    final_price = price * quantity

    print(f"{product} -> {final_price:.2f}")

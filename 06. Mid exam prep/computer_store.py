
taxes = 0
total_price_without_taxes = 0

while True:
    command = input()

    if command == 'special' or command == 'regular':
        total_price = (total_price_without_taxes + taxes)

        if command == 'special':
             total_price *= 0.9
        break

    part_price = float(command)

    if part_price <0:
        print("Invalid price!")
        continue

    total_price_without_taxes += part_price
    taxes +=0.2*part_price

if total_price == 0:
    print("Invalid order!")

else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price_without_taxes:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price:.2f}$')
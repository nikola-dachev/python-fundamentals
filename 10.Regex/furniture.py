import re

total_sum = 0
bought_furnitures = []

pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'

while True:

    command = input()

    if command == 'Purchase':
        break

    matches = re.search(pattern, command)
    if matches:
        furniture, price, quantity = matches.groups()
        bought_furnitures.append(furniture)
        total_sum += float(price) * int(quantity)

print(f'Bought furniture:')
for fur in bought_furnitures:
    print(fur)
print(f'Total money spend: {total_sum:.2f}')

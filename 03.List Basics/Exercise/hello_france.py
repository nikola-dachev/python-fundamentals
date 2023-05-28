collection_of_items = input().split('|')
budget = float(input())

bought_items = []
spent_money = 0

for item in collection_of_items:
    cloth, price = item.split('->')
    price = float(price)

    if budget < price:
        continue

    if cloth == 'Clothes':
        if price <=50.00:
            bought_items.append(price*1.4)
            budget -= price
            spent_money +=price
        else:
            continue

    elif cloth == 'Shoes':
        if price <= 35.00:
            bought_items.append(price * 1.4)
            budget -= price
            spent_money += price
        else:
            continue

    elif cloth == 'Accessories':
        if price <= 20.50:
            bought_items.append(price * 1.4)
            budget -= price
            spent_money += price
        else:
            continue

for item in bought_items:
    print(f'{item:.2f}', end=' ')
print('')
print(f"Profit: {sum(bought_items) - spent_money:.2f}")

final_budget = sum(bought_items) + budget
if final_budget >=150:
    print("Hello, France!")
else:
    print("Not enough money.")
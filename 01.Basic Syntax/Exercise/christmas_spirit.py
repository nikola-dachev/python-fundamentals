quantity_decorations = int(input())
remaining_days = int(input())
total_cost = 0
total_spirit =0

for day in range(1,remaining_days+1):

    if day % 11 == 0:
        quantity_decorations +=2

    if day % 2 == 0:
        total_cost += 2* quantity_decorations
        total_spirit += 5
    if day % 3 == 0:
        total_cost += (5 * quantity_decorations) + (3 * quantity_decorations)
        total_spirit += 13
    if day % 5 == 0:
        total_cost += 15 * quantity_decorations
        total_spirit += 17
        if day % 3 == 0:
            total_spirit +=30

    if day % 10 == 0:
        total_spirit -=20
        total_cost += 5 + 3 + 15
if remaining_days % 10 ==0:
    total_spirit -=30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")



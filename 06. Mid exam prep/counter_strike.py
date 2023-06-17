

won_battles = 0
energy = int(input())

while True:
    distance = input()

    if distance == 'End of battle':
        print(f"Won battles: {won_battles}. Energy left: {energy}")
        break

    distance = int(distance)

    if energy < distance or energy == 0:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        break
    else:
        won_battles +=1
        energy -=distance

        if won_battles % 3 == 0:
            energy += won_battles

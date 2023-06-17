people_waiting = int(input())

lift = [int(el) for el in input().split()]

for index in range(len(lift)):
    remaining_seats = 4 - lift[index]

    if people_waiting >= remaining_seats:
        people_waiting -= remaining_seats
        lift[index] = 4

    else:
        lift[index] += people_waiting
        people_waiting = 0

        print("The lift has empty spots!")
        break

if people_waiting != 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")

print(*lift)

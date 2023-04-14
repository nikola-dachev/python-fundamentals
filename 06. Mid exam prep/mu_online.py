health = 100
bitcoin = 0
dungeons_rooms = input().split('|')
room_counter = 0
is_still_alive = True

for room in dungeons_rooms:
    current_command = room.split()
    command = current_command[0]
    number = int(current_command[1])

    room_counter += 1
    if command == 'potion':

        current_health = health
        health += number
        if health > 100:
            health = 100
        print(f"You healed for {health - current_health} hp.")
        print(f"Current health: {health} hp.")

    elif command == 'chest':
        bitcoin += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number

        if health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_counter}")
            is_still_alive = False
            break
        else:
            print(f"You slayed {command}.")

if is_still_alive == True:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")

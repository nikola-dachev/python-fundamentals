rooms = int(input())
total_chairs = 0
total_visitors = 0

for room in range(1, rooms + 1):
    command = input().split()
    chairs = len(command[0])
    visitors = int(command[1])
    total_chairs += chairs
    total_visitors += visitors

    if visitors > chairs:
        print(f"{visitors - chairs} more chairs needed in room {room}")

if total_chairs >= total_visitors:
    print(f'Game On, {total_chairs - total_visitors} free chairs left')

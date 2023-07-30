
my_dict = {}
unliked_meals = 0

while True:
    command = input()

    if command == 'Stop':
        break

    current_command = command.split('-')

    action = current_command[0]
    guest = current_command[1]
    meal = current_command[2]

    if action == 'Like':
        if guest not in my_dict:
            my_dict[guest] = []

        my_dict[guest].append(meal) if meal not in my_dict[guest] else None

    elif action == 'Dislike':

        if guest not in my_dict:
            print(f"{guest} is not at the party.")

        elif meal not in my_dict[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")

        else:
            my_dict[guest].remove(meal)
            unliked_meals +=1
            print(f"{guest} doesn't like the {meal}.")


for guest, value in my_dict.items():
    print(f"{guest}: {', '.join(value)}")

print(f"Unliked meals: {unliked_meals}")

n = int(input())
my_dict = {}

for _ in range(n):
    plant, rarity = input().split('<->')

    my_dict[plant] = {'rarity': rarity, 'rating': []}

while True:
    command = input()

    if command == 'Exhibition':
        break

    current_command = command.split(': ')
    action = current_command[0]

    if action == 'Rate':
        plant, rating = current_command[1].split(' - ')
        if plant not in my_dict:
            print('error')
        else:
            my_dict[plant]['rating'].append(int(rating))


    elif action == 'Update':
        plant, new_rarity = current_command[1].split(' - ')

        if plant not in my_dict:
            print('error')
        else:
            my_dict[plant]['rarity'] = new_rarity

    elif action == 'Reset':
        plant = current_command[1]

        if plant not in my_dict:
            print('error')

        else:
            my_dict[plant]['rating'] = []

print('Plants for the exhibition:')

for key, value in my_dict.items():

    if len(my_dict[key]['rating']) > 0:
        average_rating = sum(my_dict[key]['rating']) / len(my_dict[key]['rating'])

    else:
        average_rating = 0

    print(f"- {key}; Rarity: {my_dict[key]['rarity']}; Rating: {average_rating:.2f}")



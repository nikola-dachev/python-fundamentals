jeday_dict = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    if ' | ' in command:
        current_command = command.split(' | ')
        force_side = current_command[0]
        force_user = current_command[1]

        user_exists = False

        for value in jeday_dict.values():
            if force_user in value:
                user_exists = True
                break

        if user_exists == False:
            if force_side not in jeday_dict.keys():
                jeday_dict[force_side] = [force_user]  # value force_user is a list

            else:
                jeday_dict[force_side].append(force_user)



    elif ' -> ' in command:
        current_command = command.split(' -> ')
        force_user = current_command[0]
        force_side = current_command[1]

        for key, value in jeday_dict.items():
            if force_user in value:
                jeday_dict[key].pop(value.index(force_user))
                break
        if force_side not in jeday_dict.keys():
            jeday_dict[force_side] = [force_user]
        else:
            jeday_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for force_side, force_user in jeday_dict.items():  # force_user is list !!!
    if len(jeday_dict[force_side]) > 0:
        print(f"Side: {force_side}, Members: {len(jeday_dict[force_side])}")
        for user in force_user:
            print(f"! {user}")
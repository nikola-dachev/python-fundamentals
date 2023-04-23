my_dict = {"shards": 0, "fragments": 0, "motes": 0}

is_obtained = False

while True:
    command = input().split()
    for index in range(0, len(command), 2):
        value = int(command[index])
        key = command[index + 1].lower()

        if key not in my_dict:
            my_dict[key] = 0

        my_dict[key] += value

        if my_dict["shards"] >= 250:
            print(f"Shadowmourne obtained!")
            my_dict["shards"] -= 250
            is_obtained = True

        elif my_dict["fragments"] >= 250:
            print(f"Valanyr obtained!")
            my_dict["fragments"] -= 250
            is_obtained = True

        elif my_dict["motes"] >= 250:
            print(f"Dragonwrath obtained!")
            my_dict["motes"] -= 250
            is_obtained = True

        if is_obtained:
            break
    if is_obtained:
        break

for key, value in my_dict.items():
    print(f"{key}: {value}")

target_list = [int(el) for el in input().split()]
shot_targets = 0

while True:
    command = input()
    if command == 'End':
        print(f'Shot targets: {shot_targets} -> {" ".join(str(el) for el in target_list)}')
        break
    number_index = int(command)

    if 0 <= number_index < len(target_list):
        shot_targets +=1

        for index in range(len(target_list)):
            if index != number_index:
                if target_list[index] > 0:
                    if target_list[index] > target_list[number_index]:
                        target_list[index] -= target_list[number_index]
                    else:
                        target_list[index] += target_list[number_index]

        target_list[number_index] = -1

numbers = [int(el) for el in input().split()]
average_num = float(f'{sum(numbers) / len(numbers):.2f}')

sorted_numbers = sorted(numbers, key=lambda x: -x)

counter = 0
my_list = []
for number in sorted_numbers:
    if number > average_num:
        my_list.append(number)
        counter += 1

    if counter == 5:
        break
if len(my_list) == 0:
    print('No')
else:
    print(*my_list)


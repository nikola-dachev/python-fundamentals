sum_money = input().split(', ')
sum_money_as_digit = []
for digit in sum_money:
    sum_money_as_digit.append(int(digit))

number_of_beggars = int(input())
starting_index = 0
final_list = []

for beggar in range(number_of_beggars):
    sum_one_beggar = 0
    for  i in range(starting_index, len(sum_money_as_digit),number_of_beggars):
        sum_one_beggar += sum_money_as_digit[i]

    final_list.append(sum_one_beggar)
    starting_index += 1
print(final_list)

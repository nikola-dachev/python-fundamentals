first__sequence = input().split(', ')
second_sequence = input().split(', ')

my_list = []

for first_word in first__sequence:
  for second_word in second_sequence:
    if first_word in second_word:
      my_list.append(first_word)
      break

print(my_list)

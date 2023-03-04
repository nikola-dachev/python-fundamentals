first_string = input()
second_string = input()

result =first_string

for letter in range(len(first_string)):
    if first_string[letter] == second_string[letter]:
        continue
    result = second_string[:letter+1] + first_string[letter+1:]
    print(result)
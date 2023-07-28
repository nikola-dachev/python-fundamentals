import re

my_list = []
text = input()
pattern = r'(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1'

result = re.findall(pattern ,text)

if not result:
    print("No word pairs found!")

else:
    print(f"{len(result)} word pairs found!")

    for res in result:
        first_word = res[1]
        second_word = res[2]

        if first_word == second_word[::-1]:
            my_list.append(f"{first_word} <=> {second_word}")

if len(my_list) == 0:
    print("No mirror words!")

else:
    print("The mirror words are:")
    print(*my_list, sep = ', ')



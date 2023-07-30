import re

text = input()
pattern = r'(#|\@)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
result = re.findall(pattern,text)



result_count = 0
my_list = []

if result:
    for char in result:
        if char[1] == char[2][::-1]:
            my_list.append(f'{char[1]} <=> {char[2]}')
            result_count +=1
    if result_count == 0:
        print(f"{len(result)} word pairs found!")
        print("No mirror words!")
    else:
        print(f"{len(result)} word pairs found!")
        print("The mirror words are:")
        print(", ".join(my_list))

else:
    print("No word pairs found!")
    print("No mirror words!")
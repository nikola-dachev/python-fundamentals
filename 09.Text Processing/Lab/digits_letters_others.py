text = input()
list_strings = []
list_digits = []
list_others = []

for char in text:
    if char.isalpha():
        list_strings.append(char)
    elif char.isdigit():
        list_digits.append(char)
    else:
        list_others.append(char)

print(''.join(list_digits))
print(''.join(list_strings))
print(''.join(list_others))
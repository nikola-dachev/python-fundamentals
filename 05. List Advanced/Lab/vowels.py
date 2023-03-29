#without list comprehansions

text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
final_list = []

for char in text:
    if char.lower() not in vowels:
        final_list.append(char)

print(''.join(final_list))

# with List comprehension

text = input()
vowels = ['a', 'o', 'u', 'e', 'i']

final_list = [char for char in text if char.lower() not in vowels ]
print(''.join(final_list))
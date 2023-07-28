import re

emojii_list = []
only_cool_emojiis = []
coolness_sum = 1

text = input()

pattern = r'(\:{2}|\*{2})([A-Z][a-z]{2,})(\1)'
pattern_1 = r'\d+'

result = re.findall(pattern, text)
result_1 = re.findall(pattern_1, text)

result_1 = ''.join(result_1)

for el in result_1:
    coolness_sum *= int(el)

for item in result:
    emojii_list.append(item[1])
    emojii_coolness = 0

    for char in item[1]:
        emojii_coolness += ord(char)

    if emojii_coolness >= coolness_sum:
        only_cool_emojiis.append(item)

print(f"Cool threshold: {coolness_sum}")
print(f"{len(emojii_list)} emojis found in the text. The cool ones are:")
for el in only_cool_emojiis:
    print(''.join(el))


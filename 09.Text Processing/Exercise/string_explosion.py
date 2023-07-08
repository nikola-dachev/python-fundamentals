text = input()
new_text = ''
strenght = 0

for index in range(len(text)):

    if strenght > 0 and text[index] != '>':
        strenght -= 1

    elif text[index] == '>':
        new_text += text[index]  # text[index] in this case will be actually '>'
        strenght += int(text[index + 1])

    else:
        new_text += text[index]

print(new_text)

text = input().split()
result = 0
for word in text:
    first_letter = word[0]
    last_letter = word[-1]
    current_number = int(word[1:len(word) - 1])

    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        result += (current_number / first_letter_position)

    elif first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        result += (current_number * first_letter_position)

    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        result -= last_letter_position

    elif last_letter.islower():
        last_letter_position = ord(last_letter) - 96
        result += last_letter_position

print(f'{result:.2f}')

text = input()
last_letter = ''
final_text = ''

for letter in text:
  if letter != last_letter:
    final_text +=letter
    last_letter = letter

print(final_text)

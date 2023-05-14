text = input()
new_text =''
new_symbol =''
for char in text:
  new_symbol += chr(ord(char) + 3)
new_text += new_symbol

print(new_text)

import re

total_len = 0
destination_list = []
text = input()
pattern = r'(\=|\/)([A-Z][A-Za-z]{2,})(\1)'

result = re.findall(pattern, text)

for el in result:
  total_len += len(el[1])
  destination_list.append(el[1])


print(f"Destinations: {', '.join(destination_list)}")
print(f"Travel Points: {total_len}")

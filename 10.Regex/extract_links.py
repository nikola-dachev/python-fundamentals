import re

final_list = []

pattern = r'(w{3}\.[A-Za-z0-9]+(\-*[A-Za-z0-9]+)+(\.[a-z]+\.?[a-z]*)+)'

while True:
    text = input()

    if not text:
        break

    result = re.findall(pattern, text)

    for res in result:
        final_list.append(res[0])

print('\n'.join(final_list))


import re

command = input()

while command:

    pattern = r'\d+'
    result = re.findall(pattern, command)
    if result:
        print(' '.join(result), end=" ")
    command = input()

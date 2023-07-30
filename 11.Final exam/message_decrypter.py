import re

n = int(input())
pattern = r'^(\$|\%)([A-Z][a-z]{2,})\1\:\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$'

for _ in range(n):
    text = input()

    result = re.findall(pattern, text)

    if result:
        for char in result:
            tag = char[1]
            first_num = chr(int(char[2]))
            second_num = chr(int(char[3]))
            third_num = chr(int(char[4]))
            print(f"{tag}: {first_num}{second_num}{third_num}")

    else:
        print("Valid message not found!")
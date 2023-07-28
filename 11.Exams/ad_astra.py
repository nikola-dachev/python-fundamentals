import re

text = input()
pattern = r'(\||#)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'

result = re.findall(pattern, text)

total_calories = 0

for item in result:
    total_calories += int(item[3])

days_to_endure = total_calories // 2000

print(f"You have food to last you for: {days_to_endure} days!")
for item in result:
    print(f"Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}")


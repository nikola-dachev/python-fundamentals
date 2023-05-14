import re

text = input()
pattern = r'([|\#])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1'
result = re.findall(pattern, text)

products_list = []
total_calories = 0

if result:
    for single_item in result:
        item_name = single_item[1]
        expiration_date = single_item[2]
        calories = int(single_item[3])

        products_list.append(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")

        total_calories += calories

days_to_endure = total_calories // 2000

print(f'You have food to last you for: {days_to_endure} days!')
for item in products_list:
    print(item)

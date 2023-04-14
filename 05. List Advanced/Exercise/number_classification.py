
#WITH COMPREHANSION

numbers_as_string = input().split(', ')


positive_numbers = [el for el in numbers_as_string if int(el)>=0]
negative_numbers = [el for el in numbers_as_string if int(el)< 0]
even_numbers = [el for el in numbers_as_string if int(el) % 2 == 0]
odd_numbers = [el for el in numbers_as_string if int(el) %2 != 0]


print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negative_numbers)}")
print(f"Even: {', '.join(even_numbers)}")
print(f"Odd: {', '.join(odd_numbers)}")



# WITHOUT COMPREHENSION
#
# numbers_as_string = input().split(', ')
#
#
# positive_numbers = []
# negative_numbers = []
# even_numbers = []
# odd_numbers = []
#
# for el in numbers_as_string:
# 	if int(el) >= 0:
# 		positive_numbers.append(el)
#
# 	if int(el)<0:
# 		negative_numbers.append(el)
#
# 	if int(el) % 2 == 0:
# 		even_numbers.append(el)
#
# 	if int(el) % 2 != 0:
# 		odd_numbers.append(el)
#
# print(f"Positive: {', '.join(positive_numbers)}")
# print(f"Negative: {', '.join(negative_numbers)}")
# print(f"Even: {', '.join(even_numbers)}")
# print(f"Odd: {', '.join(odd_numbers)}")



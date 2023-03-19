number = input().split()
number_as_digit = []
for element in number:
    number_as_digit.append(int(element))

number_to_remove = int(input())

for num in range (number_to_remove):
    min_number = min(number_as_digit)
    number_as_digit.remove(min_number)

number_as_string = []
for element in number_as_digit:
    number_as_string.append(str(element))
print(', '.join(number_as_string))

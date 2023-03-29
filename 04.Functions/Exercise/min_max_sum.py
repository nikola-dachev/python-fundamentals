list_as_string = input().split()
list_as_digit = []
for element in list_as_string:
  list_as_digit.append(int(element))

min_number = min(list_as_digit)
max_number = max(list_as_digit)
sum_of_numbers = sum(list_as_digit)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_of_numbers}")

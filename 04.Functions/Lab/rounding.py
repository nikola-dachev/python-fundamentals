my_list_as_string = input().split()
my_list_as_digit = []

for element in my_list_as_string:
  my_list_as_digit.append(round(float(element)))

print(my_list_as_digit

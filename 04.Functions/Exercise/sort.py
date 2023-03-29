list_as_string = input().split()
list_as_digit = []

for element in list_as_string:
  list_as_digit.append(int(element))

list_as_digit.sort()

print(list_as_digit)

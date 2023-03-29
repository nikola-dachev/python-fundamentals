def is_even(num):
  return num % 2 == 0


number_as_string = input().split()
number_as_digit = []
for element in number_as_string:
  number_as_digit.append(int(element))

print(list(filter(is_even,number_as_digit)))

my_list = input().split()
string = ''.join(my_list)

my_dict= {}

for char in string:
  if char not in my_dict:
    my_dict[char] = 0

  my_dict[char] += 1

for key, value in my_dict.items():
  print(f"{key} -> {value}")

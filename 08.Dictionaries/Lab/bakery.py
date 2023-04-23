my_list = input().split()
my_dict = {}

for index in range(0,len(my_list),2):
  key = my_list[index]
  value = int(my_list[index +1 ])
  my_dict[key] = value

number = int(input())
my_list = []
counter = 1
while True:
  result = 2 * (counter **2)
  if result < number:
    number -= result
    my_list.append(result)
  else:
    my_list.append(number)
    break
  counter +=1

print(my_list)

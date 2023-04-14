import math

numbers_as_string = input().split(', ')
numbers = [int(num) for num in numbers_as_string]

low_boundery = 1
high_boundery = 10

max_range = math.ceil(max(numbers)/10)

for index in range(1,max_range+1):
  final_list = [x for x in numbers if low_boundery<=x<=high_boundery]
  print(f"Group of {index*10}'s: {final_list}")

  low_boundery += 10
  high_boundery += 10

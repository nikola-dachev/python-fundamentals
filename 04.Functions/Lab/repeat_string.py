def calculate_func(string_input,num):
  result = string_input * num
  return result


string = input()
counter = int(input())
res = calculate_func(string, counter)
print(res)

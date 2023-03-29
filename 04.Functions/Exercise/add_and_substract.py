def sum_numbers(num1,num2):
  sum_first_two_digits = num1 +num2
  return sum_first_two_digits

def subtract(sum_first_two_digits,num3):
  result = sum_first_two_digits - num3
  return result

def add_and_subtract(num1,num2,num3):
  sum_first_func = sum_numbers(num1,num2)
  result_second_func = subtract(sum_first_func,num3)
  return result_second_func

first_number= int(input())
second_number = int(input())
third_number = int(input())
res = add_and_subtract(first_number,second_number,third_number)
print(res)

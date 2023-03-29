def smallest_number(num1, num2, num3):
    my_list = [num1, num2, num3]
    return min(my_list)


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = smallest_number(first_number, second_number, third_number)
print(result)

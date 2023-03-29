# First way


def factorial(num1, num2):
    result_one = 1
    result_two = 1
    for digit in range(1, num1 + 1):
        result_one *= digit
    for digit in range(1, num2 + 1):
        result_two *= digit
    return f'{result_one / result_two:.2f}'


first_number = int(input())
second_number = int(input())
res = factorial(first_number, second_number)
print(res)

# Second way


def factorial(num):
    final_sum = 1
    for digit in range(1, num + 1):
        final_sum *= digit
    return final_sum


first_number = int(input())
second_number = int(input())
first_factorial = factorial(first_number)
second_factorial = factorial(second_number)
final_result = first_factorial / second_factorial
print(f'{final_result:.2f}')

def calculate_func(operator, first_number, second_number):
    result = 0

    if operator == 'add':
        result = first_number + second_number

    if operator == 'subtract':
        result = first_number - second_number

    if operator == 'multiply':
        result = first_number * second_number

    if operator == 'divide':
        result = int(first_number / second_number)

    return result


command_operator = input()
num_1 = int(input())
num_2 = int(input())

res = calculate_func(command_operator, num_1, num_2)
print(res)

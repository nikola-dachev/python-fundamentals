def perfect_number(num):
    sum_digits = 0
    for digit in range(1, num):
        if num % digit == 0:
            sum_digits += digit
    if sum_digits == num:
        return f'We have a perfect number!'

    else:
        return f"It's not so perfect."


number = int(input())
res = perfect_number(number)
print(res)

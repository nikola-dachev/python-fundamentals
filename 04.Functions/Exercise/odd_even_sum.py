def odd_even_sum(num):
    sum_even = 0
    sum_odd = 0
    for digit in num:
        if int(digit) % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)

    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


number = input()
print(odd_even_sum(number))

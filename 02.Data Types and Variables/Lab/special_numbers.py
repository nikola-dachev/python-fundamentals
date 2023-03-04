n = int(input())

for num in range(1,n+1):
    sum_digits = 0
    for digit in str(num):
        sum_digits += int(digit)
    if sum_digits == 5 or sum_digits ==7 or sum_digits == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
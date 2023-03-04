import sys

first_number = int(input())
second_number = int(input())
max_number = - sys.maxsize

for i in range(first_number, second_number+1):
    if i > 0 and i % first_number == 0:
        max_number =i

print(max_number)
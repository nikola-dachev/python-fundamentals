n = int(input())

for i in range(0,n):
    number= int(input())

    if number % 2 != 0:
        print(f"{number} is odd!")
        break
else:
    print(f"All numbers are even.")
budget = int(input())

while True:
    command = input()

    if command =='End':
        print(f"You bought everything needed.")
        break
    price = int(command)

    budget -=price

    if budget < 0:
        print(f"You went in overdraft!")
        break

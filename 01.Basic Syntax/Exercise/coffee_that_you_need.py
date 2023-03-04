number_of_coffees = 0

while True:
    command = input()

    if command == 'END':
        print(f'{number_of_coffees}')
        break
    
    if command =='coding' or command =='cat' or command =='dog' or command =='movie':
        number_of_coffees +=1
    elif command =='CODING' or command =='CAT' or command =='DOG' or command =='MOVIE':
        number_of_coffees +=2
    else:
        continue

    if number_of_coffees >5:
        print(f"You need extra sleep")
        break



n = int(input())

for i in range(0,n):
    current_number = int(input())

    if current_number == 88:
        print("Hello")
    elif current_number == 86:
        print(f"How are you?")
    elif current_number < 88:
        print("GREAT!")
    elif current_number >88:
        print("Bye.")
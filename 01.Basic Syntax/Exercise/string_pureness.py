n = int(input())

for i in range(0,n):
    text = input()

    if "," in text:
        print(f"{text} is not pure!")
    elif "." in text:
        print(f"{text} is not pure!")
    elif "_" in text:
        print(f"{text} is not pure!")
    else:
        print(f"{text} is pure.")

text = input().split()
first_string = text[0]
second_string = text[1]
result = 0

if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        result += ord(first_string[index]) * ord(second_string[index])

    for index in range(len(second_string), len(first_string)):
        result += ord(first_string[index])

elif len(first_string) < len(second_string):
    for index in range(len(first_string)):
        result += ord(first_string[index]) * ord(second_string[index])

    for index in range(len(first_string), len(second_string)):
        result += ord(second_string[index])

elif len(first_string) == len(second_string):
    for index in range(len(first_string)):
        result += ord(first_string[index]) * ord(second_string[index])

print(result)

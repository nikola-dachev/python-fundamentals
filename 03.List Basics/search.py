n = int(input())
special_word = input()
my_list = []
filtered_list = []
for i in range(n):
    command= input()
    my_list.append(command)

    if special_word in command:
        filtered_list.append(command)

print(my_list)
print(filtered_list)
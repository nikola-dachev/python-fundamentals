factor = int(input())
count = int(input())
my_list = []
for num in range(1, count+1):
    result = num * factor
    my_list.append(result)
print(my_list)
# #without list comprehension

numbers_as_string = input().split(', ')
numbers=[]
final_list =[]

for el in numbers_as_string:
    numbers.append(int(el))

for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        final_list.append(index)

print(final_list)


#with list comprehension

numbers_as_string = input().split(', ')
final_list = [index for index in range(len(numbers_as_string)) if int(numbers_as_string[index]) % 2 ==0]
print(final_list)

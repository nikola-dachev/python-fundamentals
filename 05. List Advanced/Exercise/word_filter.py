words = input().split()
my_list = [word for word in words if len(word) % 2 == 0]
print('\n'.join(my_list))

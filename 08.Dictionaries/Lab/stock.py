my_list = input().split()
my_dict = {}
for index in range(0, len(my_list), 2):
    key = my_list[index]
    value = int(my_list[index + 1])
    my_dict[key] = value

searched_products = input().split()

for product in searched_products:
    if product in my_dict.keys():
        print(f"We have {my_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

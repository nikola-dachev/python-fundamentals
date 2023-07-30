import re

pattern =r'\@\#+[A-Z][A-Za-z0-9]{4,}[A-Z]\@\#+'
number_of_products = int(input())

for index in range(number_of_products):
    command = input()
    result = re.findall(pattern,command)
    if result:
        product_group = ''
        for char in result:
            for char1 in char:
                if char1.isdigit():
                    product_group += char1
            if product_group =='':
                product_group = '00'
            print(f'Product group: {product_group}')
    else:
        print("Invalid barcode")


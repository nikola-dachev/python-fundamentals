def calc_func(par_product, par_quantity):
    total_price = 0
    if par_product == 'coffee':
        total_price = par_quantity * 1.50
    elif par_product == 'water':
        total_price = par_quantity * 1
    elif par_product == 'coke':
        total_price = par_quantity * 1.40
    elif par_product == 'snacks':
        total_price = par_quantity * 2

    return total_price


product = input()
quantity = int(input())
res = calc_func(product, quantity)
print(f'{res:.2f}')

vehicles_list = input().split('>>')

total_collected_taxes = 0

for item in vehicles_list:
    current_item= item.split()

    vehicle_type = current_item[0]
    taxed_years = int(current_item[1])
    kilometers = int(current_item[2])

    vehicle_tax = 0

    if vehicle_type == 'family':
        possible_uplift_travel = kilometers // 3000
        vehicle_tax = possible_uplift_travel * 12 + (50 - 5* taxed_years)
        print(f"A {vehicle_type} car will pay {vehicle_tax:.2f} euros in taxes.")

    elif vehicle_type == 'heavyDuty':
        possible_uplift_travel = kilometers // 9000
        vehicle_tax = possible_uplift_travel * 14 + (80 - 8 * taxed_years)
        print(f"A {vehicle_type} car will pay {vehicle_tax:.2f} euros in taxes.")

    elif vehicle_type == 'sports':
        possible_uplift_travel = kilometers // 2000
        vehicle_tax = possible_uplift_travel * 18 + (100 - 9 * taxed_years)
        print(f"A {vehicle_type} car will pay {vehicle_tax:.2f} euros in taxes.")

    else:
        print("Invalid car type.")

    total_collected_taxes +=vehicle_tax

print(f"The National Revenue Agency will collect {total_collected_taxes:.2f} euros in taxes.")
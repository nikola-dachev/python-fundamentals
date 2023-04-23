my_dict = {}
while True:
    command = input()
    if command == 'End':
        break

    current_command = command.split(' -> ')
    company_name = current_command[0]
    employee_id = current_command[1]

    if company_name not in my_dict:
        my_dict[company_name] = []

    if employee_id not in my_dict[company_name]:
        my_dict[company_name].append(employee_id)

for company_name, employee_id in my_dict.items():
    print(f"{company_name}")
    for each_employee_id in employee_id:
        print(f"-- {each_employee_id}")

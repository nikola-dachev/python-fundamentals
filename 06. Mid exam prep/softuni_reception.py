first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())

number_of_questions = int(input())

questions_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

hours_ = 0

while number_of_questions > 0:
    hours_ += 1
    if hours_ % 4 == 0:
        continue

    number_of_questions -= questions_per_hour

print(f'Time needed: {hours_}h.')

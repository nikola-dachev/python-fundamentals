my_dict = {}
while True:
    command = input()
    if command == 'end':
        break

    current_command = command.split(' : ')
    course = current_command[0]
    student_name = current_command[1]

    if course not in my_dict:
        my_dict[course] = []

    my_dict[course].append(student_name)

for course_name, student_name in my_dict.items():
    print(f"{course_name}: {len(student_name)}")
    for student in student_name:
        print(f"-- {student}")

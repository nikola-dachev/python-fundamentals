my_dict = {}

while True:
  command = input()
  if ':' not in command:
    command = command.replace('_', ' ')
    students = my_dict[command]
    for student_id, name in students.items():
      print(f"{name} - {student_id}")
    break

  current_command = command.split(':')
  name = current_command[0]
  student_id = current_command[1]
  course = current_command[2]
  if course not in my_dict:
    my_dict[course] = {student_id : name}
  else:
    my_dict[course][student_id] = name

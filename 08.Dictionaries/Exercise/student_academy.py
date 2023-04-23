my_dict = {}
number_of_students = int(input())
for student in range(1, number_of_students +1):
  student_name = input()
  grade  =float(input())

  if student_name not in my_dict:
    my_dict[student_name] = []

  my_dict[student_name].append(grade)

for key , value in my_dict.items():
  average_grade = sum(value)/len(value)
  if average_grade >= 4.50:
    print(f"{key} -> {average_grade:.2f}")

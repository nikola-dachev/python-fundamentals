import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
top_student_attendences = 0

for student in range(1,number_of_students+1):
    count_of_attendances = int(input())

    total_bonus = count_of_attendances / number_of_lectures * (5+additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        top_student_attendences = count_of_attendances

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {top_student_attendences} lectures.")

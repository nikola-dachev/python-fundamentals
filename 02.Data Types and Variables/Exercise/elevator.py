import math

number_of_people = int(input())
capacity = int(input())

courses_count = math.ceil(number_of_people /capacity)

print(courses_count)

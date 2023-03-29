employees_happiness_string = input().split(' ')
improvement_factor = int(input())
employees_happiness_int = []
final_list = []
average = 0

for el in employees_happiness_string:
    employees_happiness_int.append(int(el))

for el in employees_happiness_int:
    average += improvement_factor * el
    final_list.append(improvement_factor * el)

average /=len(employees_happiness_int)
happy_count = 0

for el in final_list:
    if el>=average:
        happy_count +=1

if happy_count >=len(final_list)/2:
    print(f'Score: {happy_count}/{len(final_list)}. Employees are happy!')

else:
    print(f'Score: {happy_count}/{len(final_list)}. Employees are not happy!')



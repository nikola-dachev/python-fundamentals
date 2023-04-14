courses = input().split(', ')
final_list = courses

while True:
    command = input()
    if command == 'course start':
        break

    current_command = command.split(':')
    action = current_command[0]
    lesson_title = current_command[1]

    if action == 'Add':
        if lesson_title not in final_list:
            final_list.append(lesson_title)

    elif action == 'Insert':
        if lesson_title not in final_list:
            final_list.insert(int(current_command[2]), lesson_title)

    elif action == 'Remove':
        if lesson_title in final_list:
            title_index = final_list.index(lesson_title)
            if title_index + 1 in range(len(final_list)):
                if 'Exercise' in final_list[title_index + 1]:
                    final_list.pop(title_index + 1)
            final_list.remove(lesson_title)

    elif action == 'Swap':
        second_title = current_command[2]
        if lesson_title in final_list and second_title in final_list:
            first_position = final_list.index(lesson_title)
            second_position = final_list.index(second_title)
            first_has_exercise = False
            second_has_exercise = False
            if first_position + 1 in range(len(final_list)):
                first_has_exercise = 'Exercise' in final_list[first_position + 1]
            if second_position + 1 in range(len(final_list)):
                second_has_exercise = 'Exercise' in final_list[second_position + 1]
            final_list[first_position], final_list[second_position] = final_list[second_position], final_list[
                first_position]
            if first_has_exercise and second_has_exercise:
                final_list[first_position + 1], final_list[second_position + 1] = final_list[second_position + 1], \
                final_list[first_position + 1]
            elif not first_has_exercise and second_has_exercise:
                final_list.insert(first_position + 1, final_list.pop(second_position + 1))
            elif first_has_exercise and not second_has_exercise:
                final_list.insert(second_position + 1, final_list.pop(first_position + 1))
    elif action == 'Exercise':
        # first option - we have the lesson but we do not have the exercise, add only the exercise
        if lesson_title in final_list and f"{lesson_title}-Exercise" not in final_list:
            lesson_index = final_list.index(lesson_title)
            final_list.insert(lesson_index + 1, f"{lesson_title}-Exercise")
        # second option the lesson is not on the list - add both lesson and exercise
        elif lesson_title not in final_list:
            final_list.append(lesson_title)
            final_list.append(f"{lesson_title}-Exercise")

for index, lesson_name in enumerate(final_list):
    print(f'{index + 1}.{lesson_name}')

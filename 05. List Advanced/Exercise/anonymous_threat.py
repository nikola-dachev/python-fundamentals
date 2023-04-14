text = input().split()
final_list = text

while True:
    command = input()
    if command == "3:1":
        print(' '.join(final_list))
        break

    current_command = command.split()
    action = current_command[0]

    if action == 'merge':
        start_index = int(current_command[1])
        end_index = int(current_command[2])

        start_index = max(0, start_index)
        end_index = min(len(text) - 1, end_index)

        merged_elements = ''
        for index in range(start_index, end_index + 1):
            merged_elements += text[index]

        for _ in range(start_index, end_index + 1):
            text.pop(start_index)
        text.insert(start_index, merged_elements)

    elif action == 'divide':
        index = int(current_command[1])
        partitions = int(current_command[2])

        el_to_divide = text[index]
        list_for_divided_el = []
        partition_size = len(el_to_divide) // partitions

        current_partition = ''
        for idx in range((partitions - 1) * partition_size):
            current_partition += el_to_divide[idx]
            if len(current_partition) == partition_size:
                list_for_divided_el.append(current_partition)
                current_partition = ''

        current_partition = ''
        for idx in range((partitions - 1) * partition_size, len(el_to_divide)):
            current_partition += el_to_divide[idx]

        list_for_divided_el.append(current_partition)

        text.pop(index)
        for idx in range(len(list_for_divided_el)):
            text.insert(index + idx, list_for_divided_el[idx])

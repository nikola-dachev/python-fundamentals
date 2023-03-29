def char_in_range(first, second):
    my_list = []
    for current_char in range(ord(first) + 1, ord(second)):
        my_list.append(chr(current_char))
    return my_list


first_char = input()
second_char = input()
res = char_in_range(first_char, second_char)
print(' '.join(res))

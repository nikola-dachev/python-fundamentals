text = input().upper()
final_text = ''
current_symbols = ''
repetitions = ''

for index in range(len(text)):
    if not text[index].isdigit():
        current_symbols += text[index]

    else:
        for new_symbol_index in range(index, len(text)):
            if not text[new_symbol_index].isdigit():
                break
            repetitions += text[new_symbol_index]

        final_text +=current_symbols * int(repetitions)
        current_symbols= ''
        repetitions = ''

print(f'Unique symbols used: {len(set(final_text))}')
print(final_text)
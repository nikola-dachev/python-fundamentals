start_char_index = int(input())
final_char_index = int(input())
char = ''


for i in range(start_char_index, final_char_index +1):
	char = chr(i)
	print(char,end=' ')

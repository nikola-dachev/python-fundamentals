number_of_chars = int(input())
total_sum = 0

for i in range(0,number_of_chars):
	char = input()
	total_sum +=ord(char)

print(f"The sum equals: {total_sum}")


import sys

number_snowballs = int(input())
max_value = -sys.maxsize
max_weight = -sys.maxsize
max_time =  -sys.maxsize
max_quality = -sys.maxsize

for i in range(number_snowballs):

	snowball_weight= int(input())
	snowball_time = int(input())
	snowball_quality = int(input())

	snowball_value = (snowball_weight / snowball_time) ** snowball_quality

	if snowball_value > max_value:
		max_value = int(snowball_value)
		max_weight = snowball_weight
		max_time  = snowball_time
		max_quality = snowball_quality

print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")

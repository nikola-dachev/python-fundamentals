import re

text = input()
pattern = r'(\=|\/)([A-Z][A-Za-z]{2,})\1'
result = re.findall(pattern,text)
travel_points = 0
my_list = []

if result:
  for res in result:
    country = res[1]
    my_list.append(country) #adding all countries to a list that i will unpack when printing
    travel_points += len(country)
print(f"Destinations: {', '.join(my_list)}")
print(f"Travel Points: {travel_points}")

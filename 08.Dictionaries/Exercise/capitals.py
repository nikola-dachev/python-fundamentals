country_name = input().split(', ')
capital_city = input().split(', ')
my_dict = {country_name[index] : capital_city[index] for index in range(len(country_name))}

for key , value in my_dict.items():
  print(f"{key} -> {value}")

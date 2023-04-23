words = [el.lower() for el in input().split()]
default_value = 0

my_dict = dict.fromkeys(words, default_value)

for word in words:
  my_dict[word] +=1

for key , value in my_dict.items():
  if value % 2 != 0:
    print(key, end=' ')

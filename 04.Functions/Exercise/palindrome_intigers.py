def myfunc(list):
  for num in list:
    if num == num[::-1]:
      print('True')
    else:
      print('False')


list_as_string = input().split(', ')

myfunc(list_as_string)

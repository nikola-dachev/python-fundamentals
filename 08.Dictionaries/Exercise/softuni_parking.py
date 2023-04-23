number_of_cars = int(input())
my_dict = {}

for car in range(number_of_cars):
  command = input().split()
  action = command[0]
  username = command[1]

  if action =='register':
    license_plate = command[2]
    if username not in my_dict:
      my_dict[username] = license_plate
      print(f"{username} registered {license_plate} successfully")
    else:
      print(f"ERROR: already registered with plate number {license_plate}")

  elif action == 'unregister':
    if username not in my_dict:
      print(f"ERROR: user {username} not found")
    else:
      print(f"{username} unregistered successfully")
      my_dict.pop(username)

for username, license_plate in my_dict.items():
  print(f"{username} => {license_plate}")

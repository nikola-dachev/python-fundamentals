initial_route = input()

while True:
  command = input()

  if command =='Travel':
    print(f"Ready for world tour! Planned stops: {initial_route}")
    break

  current_command = command.split(':')
  action = current_command[0]

  if action =='Add Stop':
    index = int(current_command[1])
    string = current_command[2]
    if 0 <= index < len(initial_route):
      initial_route = initial_route[:index] + string + initial_route[index:]
    print(f'{initial_route}') # we are always printing even if the index is not valid

  elif action == 'Remove Stop':
    start_index = int(current_command[1])
    end_index = int(current_command[2])
    if 0 <= start_index < len(initial_route) and 0<= end_index < len(initial_route):
      initial_route = initial_route[:start_index] + initial_route[end_index+1:]
    print(f'{initial_route}') # we are always printing even if the index is not valid

  elif action =='Switch':
    old_string = current_command[1]
    new_string = current_command[2]
    if old_string in initial_route:
      initial_route = initial_route.replace(old_string, new_string)
    print(f'{initial_route}') # we are always printing even if the index is not valid

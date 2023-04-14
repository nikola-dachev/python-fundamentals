version_as_string = input().split('.')
version = [int(num)for num in version_as_string]
version[-1] += 1

for index in range(len(version)-1,-1,-1):
  if version[index] >9:
    version[index] = 0
    if index - 1 >=0:
      version[index -1] +=1
version_back_to_string = [str(num)for num in version]
print('.'.join(version_back_to_string))

text = input().split('\\')
files = text[-1].split('.')
file_name = files[0]
extension = files[1]


print(f'File name: {file_name}')
print(f'File extension: {extension}')

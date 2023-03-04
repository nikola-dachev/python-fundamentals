result = ''
while True:
    text = input()

    if text =='SoftUni':
        continue
    if text == 'End':
        break

    for letter in text:
        result +=letter * 2
    print(result)
    result = ''
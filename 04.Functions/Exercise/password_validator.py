def pass_validator(my_pass):
    pass_is_valid = True
    if len(my_pass) < 6 or len(my_pass) > 10:
        pass_is_valid = False
        print(f'Password must be between 6 and 10 characters')

    if not my_pass.isalnum():
        pass_is_valid = False
        print(f'Password must consist only of letters and digits')

    counter = 0
    for char in my_pass:
        if char.isdigit():
            counter += 1
    if counter < 2:
        pass_is_valid = False
        print(f'Password must have at least 2 digits')

    return pass_is_valid


password = input()
result = pass_validator(password)
if result == True:
    print("Password is valid")

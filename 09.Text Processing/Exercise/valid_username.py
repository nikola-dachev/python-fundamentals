def correct_lenght(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def correct_symbols(name):
    for char in name:
        if not (char.isalnum() or char == '-' or char == '_'):
            return False
    return True


def noredundent_symbols(name):
    if ' ' not in name:
        return True
    return False


def is_username_valid(name):
    if correct_lenght(name) and correct_symbols(name) and noredundent_symbols(name):
        return True
    return False


usernames = input().split(', ')
for username in usernames:
    if is_username_valid(username):
        print(username)

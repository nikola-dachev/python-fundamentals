year = int(input())
year += 1

while True:
    year_as_string = str(year)

    if len(year_as_string) != len(set(year_as_string)):
        year += 1

    else:
        print(year)
        break


import re

text = input()
pattern = r"\b(?P<day>\d{2})(\/|.|-)(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
result = re.finditer(pattern,text)

for date in result:
  date_data = date.groupdict()
  print(f"Day: {date_data['day']}, Month: {date_data['month']}, Year: {date_data['year']}")

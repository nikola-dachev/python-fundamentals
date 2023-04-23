count = int(input())
synonims = {}
for _ in range(count):
  key = input()
  value = input()
  if key not in synonims:
    synonims[key] = []
  synonims[key].append(value)

for key, value in synonims.items():
  print(f"{key} - {', '.join(value)}")

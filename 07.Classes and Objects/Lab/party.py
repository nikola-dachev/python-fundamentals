class Party:
  def __init__(self):
    self.people = []

party_object = Party()

while True:
  command = input()
  if command == 'End':
    print(f"Going: {', '.join(party_object.people)}")
    print(f"Total: {len(party_object.people)}")
    break

  party_object.people.append(command)

class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):

        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo._Zoo__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo._Zoo__animals}"

        elif species == 'fish':
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo._Zoo__animals}"

        elif species == 'bird':
            return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo._Zoo__animals}"


zoo_name = input()
number_of_animals = int(input())
zoo = Zoo(zoo_name)

for animal in range(number_of_animals):
    command = input().split()
    species = command[0]
    name = command[1]
    zoo.add_animals(species, name)

final_species = input()
print(zoo.get_info(final_species))


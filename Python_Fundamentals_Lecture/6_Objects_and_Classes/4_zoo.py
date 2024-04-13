class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            names = ', '.join(self.mammals)
        elif species == "fish":
            names = ', '.join(self.fishes)
        elif species == "bird":
            names = ', '.join(self.birds)
        else:
            names = "Invalid species"

        return f"{species.capitalize()}s in {self.name}: {names}\nTotal animals: {Zoo.__animals}"


zoo_name = input()

zoo = Zoo(zoo_name)

num_animals = int(input())

for _ in range(num_animals):
    animal_info = input().split()
    species, name = animal_info[0], animal_info[1]
    zoo.add_animal(species, name)

requested_species = input()

print(zoo.get_info(requested_species))

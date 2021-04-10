class Pet:
    """Create a new Pet"""
    def __init__(self, name, animal):
        self.name = name
        self.animal = animal

newPet = Pet("Bingo", "Chihuahua")

print(newPet)
print(newPet.name)
print(newPet.animal)

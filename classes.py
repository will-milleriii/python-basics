class Pet:
    """Create a new Pet"""
    def __init__(self, name, animal):
        self.name = name
        self.animal = animal

newPet = Pet("Bingo", "Chihuahua")
newestPet = Pet("Gracie", "Goldendoodle")

newPet.name = "Flare"
newPet.animal = "Cairn Terrier"

del newestPet

print(newPet.name)
print(newPet.animal)
#print(newestPet.name)
#print(newestPet.animal)

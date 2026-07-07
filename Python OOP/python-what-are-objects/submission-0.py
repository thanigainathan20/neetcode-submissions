class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
            self.name = name
            self.species = species
            self.hunger = hunger
            self.energy = energy


# Don't modify the above code

whiskers_pet = Pet("Whiskers", "cat", 6, 8)

# TODO: Create a pet named "Whiskers" that is a species of 'cat' with hunger level 6 and energy level 8


# Don't modify the following code
print(f"{whiskers_pet.name} ({whiskers_pet.species}) - Hunger: {whiskers_pet.hunger}, Energy: {whiskers_pet.energy}") 

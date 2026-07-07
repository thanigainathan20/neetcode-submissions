class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def make_sound(self):
        print("Animal is making a sound")

class Dog(Animal):
    def __init__(self, name: str, sound_type: str):
        super().__init__(name)
        self.sound_type = sound_type

    def make_sound(self):
        print(f"{self.name} says: {self.sound_type}")

class Cat(Animal):
    def __init__(self, name: str, sound_type: str):
        super().__init__(name)
        self.sound_type = sound_type

    def make_sound(self) -> None:
        print(f"{self.name} says: {self.sound_type}")


# Test the code
animal = Animal("Rabbit")
animal.make_sound()

animal = Dog("Buddy", "Woof!")
animal.make_sound()

animal = Cat("Whiskers", "Meow!")
animal.make_sound()



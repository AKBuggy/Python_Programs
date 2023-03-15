import animal as animal


class Dog(animal.Animal):
    species = "Labrador"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print(f"My name is {self.name} and {self.age} years old and I come from species called {self.species}")

    def speaks(self, sound):
        print(f"{self.name} says {sound}")

    @staticmethod
    def barks():
        print("I bark for protection whereas humans bark for useless things")

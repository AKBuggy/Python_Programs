from multipledispatch import dispatch


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

    def fetch(self, item):
        return f"{self.name} fetches {item}"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

    def chase_mouse(self):
        return f"{self.name} chases a mouse"


class Bird(Animal):
    def speak(self):
        return f"{self.name} says Chirp!"

    def fly(self):
        return f"{self.name} flies away"


# Overloading example
class Calculator:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c


# Overriding example
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def area(self):
        return self.length ** 2


if __name__ == "__main__":
    # Inheritance example
    dog = Dog("Buddy")
    print(dog.speak())
    print(dog.fetch("stick"))

    cat = Cat("Whiskers")
    print(cat.speak())
    print(cat.chase_mouse())

    bird = Bird("Tweetie")
    print(bird.speak())
    print(bird.fly())

    # Overloading example
    calculator = Calculator()
    print(calculator.add(2, 3))
    print(calculator.add(2, 3, 4))

    # Overriding example
    rectangle = Rectangle(4, 5)
    print(rectangle.area())

    square = Square(4)
    print(square.area())

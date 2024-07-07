# 1. Write a Python program to create a class representing a Circle.
# Include methods to calculate its area and perimeter.

# perimeter of circle -> 2πr
# area of circle -> πr2

# create class Circle
class Circle:
    # Initialize the Circle object with a given radius
    def __init__(self, radius):
        self.radius = radius

    # perimeter method
    def perimeter(self):
        return 2 * (22 / 7) * self.radius

    # area method
    def area(self):
        return (22 / 7) * (self.radius ** 2)


def main():
    rad = float(input("Enter radius to find perimeter and area of a circle: "))
    circle = Circle(rad)
    print(f"Perimeter of circle is: {circle.perimeter():.2f}")
    print(f"Area of circle is: {circle.area():.2f}")


if __name__ == '__main__':
    main()

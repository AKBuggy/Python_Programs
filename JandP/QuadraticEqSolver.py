import math


class QuadraticEquationSolver:
    def findRoots(self, a, b, c):
        # Calculate the discriminant
        discriminant = b ** 2 - 4 * a * c
        # Check if the discriminant is negative, indicating no real roots
        if discriminant < 0:
            return "No real roots"
        elif discriminant == 0:
            # If discriminant is zero, both roots are the same
            root = -b / (2 * a)
            return root
        else:
            # Calculate both roots
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return root1, root2


# Accept coefficients of the quadratic equation from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Create an instance of QuadraticEquationSolver
solver = QuadraticEquationSolver()
# Call the findRoots method and print the roots
roots = solver.findRoots(a, b, c)
print("Roots:", roots)

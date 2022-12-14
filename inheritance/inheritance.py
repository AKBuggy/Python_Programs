class Vehicle:
    def general_usage(self):
        print("General usage: Transportation")


class Car(Vehicle):
    def __init__(self):
        print("I'm a car")
        self.wheels = 4
        self.roof = True
        print("Wheels =", self.wheels,
              "Roof =", self.roof
              )

    def specific_usage(self):
        print("Specific usage: commute to work, vacation with family")


class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm a motor cycle")
        self.wheels = 2
        self.roof = False
        print("Wheels =", self.wheels,
              "Roof =", self.roof
              )

    def specific_usage(self):
        print("Specific usage: road trip, racing")


print("---------------------------------------------")

c = Car()
c.general_usage()
c.specific_usage()

print("---------------------------------------------")

m = MotorCycle()
m.general_usage()
m.specific_usage()

print("---------------------------------------------")

# Checks whether the object is instance of the specific class or not
print(isinstance(c, Car))
print(isinstance(c, MotorCycle))

# Checks whether the class is the subclass of other class
print(issubclass(Car, Vehicle))
print(issubclass(MotorCycle, Vehicle))

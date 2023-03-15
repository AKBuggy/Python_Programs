from Car import Car


class Vehicle(Car):

    def __init__(self, noOfWheels, vName):
        self.noOfWheels = noOfWheels
        self.vName = vName

    def whichVehicle(self):
        if self.noOfWheels == 4:
            print("Car has 4 Wheels")
            Car.carName(self.vName)
        else:
            print(f"Car cannot have {self.noOfWheels} wheels you fool")

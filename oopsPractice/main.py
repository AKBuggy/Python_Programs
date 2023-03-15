import dog as d
import Vehicle as v


def main():
    dog = d.Dog("Miles", 9)
    dog.sleeps()
    dog.eats()
    dog.barks()
    dog.description()
    dog.speaks("Woof woof")
    print(dog.species)

    baleno = v.Vehicle(4, "Baleno")
    baleno.whichVehicle()


if __name__ == '__main__':
    main()

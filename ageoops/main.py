# 2. Write a Python program to create a person class. Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.
import datetime


class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def ageCalculator(self):
        # get current year subtract it by year of the person.
        currYear = datetime.datetime.now()
        birthYear = self.dob.split("/")[-1]
        return int(currYear.strftime("%Y")) - int(birthYear)


def main():
    name = input("Enter your name: ")
    country = input("Enter your country's name: ")
    dob = input("Enter your date of birth in this format dd/mm/yyyy: ")
    person = Person(name, country, dob)
    print(person.ageCalculator())


if __name__ == '__main__':
    main()


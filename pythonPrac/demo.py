from math import sqrt
"""
All the imports above
"""

"""
    Practise Python Codes in this files
"""


###########################################################
"""
        Adding two numbers
"""


def addTwoNumbers(no1, no2):
    print("The sum of the number is ", no1 + no2)
    print("The sum of {0} and {1} is {2} ".format(no1, no2, no1 + no2))

    # # memory efficient since not using variables but hard to read
    # print('The sum is %.1f' % (float(input('Enter first number: ')) + float(input('Enter second number: '))))


##########################################################
"""
Python program to find the sqrt of the number
"""


def findSqrRoot(inp):
    print("Square root of %0.2f is %0.2f" % (inp, sqrt(inp)))


if __name__ == '__main__':
    # easy implementation
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    addTwoNumbers(num1, num2)

    num = float(input("Enter the number to find the square root: "))
    findSqrRoot(num)

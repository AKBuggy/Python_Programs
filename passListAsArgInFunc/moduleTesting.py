# How to take list values from the user

# function for taking input from the user(list)
def take_user_input():
    lst = []
    size = int(input("Enter the size of the list: "))
    print("Enter the elements of the list: ")
    for i in range(size):
        data = int(input())
        lst.append(data)

    return lst


# How to pass list as a parameter/argument

# Function for counting even and odd numbers
def count(lst):
    evenNo = 0
    oddNo = 0

    for i in lst:
        if i % 2 == 0:
            evenNo += 1
        else:
            oddNo += 1

    return evenNo, oddNo


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        # return self.m1, self.m2  # method 1
        return '{} {} '.format(self.m1, self.m2)  # method 2


s1 = Student(50, 60)
s2 = Student(45, 45)

s3 = s1 + s2
print(s3.m1)
print(s3.m2)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

# Now we want to print the object values
# if we do like this
# print(s1.__str__())  # Now we have to modify str function in our own way  # method 1
print(s1)  # this will print the address of the object # method 2

# Point to remember
a = 10
print(a)  # This is automatically calling a.__str__()

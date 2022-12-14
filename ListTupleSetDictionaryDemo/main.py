marks = [97, 84, 78, 72]

# prints all marks from the list
print(marks)

# prints 0th index marks i.e is 1
print(marks[0])

# prints from backside since it is negative i.e 4
print(marks[-1])

# prints only till first 3 numbers
print(marks[0:3])

# print individual marks using loop
for score in marks:
    print(score)

# add new marks then you can use append
marks.append(99)
print(marks)

# add new marks inbetween some number then you can use insert
marks.insert(0, 56)
print(marks)

# to check whether the number is present or not we can use
print(99 in marks)

# to print the length of the list we can use 'len' function
print(len(marks))

# to clear a list we can make use of 'clear' function
# marks.clear()

print("-----------------------------------------------------------")

################################
# Tuple example
# Tuple declaration is with ()
# Tuple is immutable

marks = (78, 79, 80, 78)
print(marks.count(78))
print(marks.index(79))

print("-----------------------------------------------------------")

#################################
# Set example
# Set declaration is with {}
# You can't access values by writing index eg this won't work marks[1]
# Set always prints unique values will exclude repeating values

marks = {56, 56, 78, 90}
print(marks)

print("-----------------------------------------------------------")

##################################
# Dictionary example
# Dictionary declaration is with {}
# Dictionary can be used for storing key-value pairs
# Dictionary can add new key-value pairs, or change the existing values

marks = {"English": 87, "Maths": 97}
print(marks["Maths"])
marks["BK"] = 87
print(marks)

marks["English"] = 90
print(marks)

print("-------------------------------------")
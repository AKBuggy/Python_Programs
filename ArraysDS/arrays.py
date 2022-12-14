import math

household_exp = [2200, 2350, 2600, 2130, 2190]
print(household_exp)

# Question 1
extraExpInFeb = household_exp[1] - household_exp[0]
print("Extra Rs", extraExpInFeb, "more than Jan")

# Question 2
for i in range(0, 4):
    totalQuarterExp = household_exp[i]

# Question 3
print("Total expense that occur till quarter is Rs", totalQuarterExp)

# Question 4
print("Did I spent Rs 2000 in any month:", 2000 in household_exp)

# Question 5
household_exp.append(1980)
print(household_exp)

# Question 6
household_exp[3] = household_exp[3] - 200
print(household_exp)

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# Question 1
print(len(heros))

# Question 2
heros.append("black panther")
print(heros)

# Question 3
heros.remove("black panther")
heros.insert(2, "black panther")
print(heros)

# Question 4
heros[1:3] = ['doctor strange']
print(heros)

# Question 5
heros.sort()
print(heros)


maxOddInput = int(input("Enter the max odd number as per your wish: "))

if maxOddInput % 2 == 0:
    print("Enter odd max number!!", maxOddInput, "is an even number.")
    exit()
else:
    collectionsOfOddNo = []
    maxSizeOfList = math.ceil(maxOddInput / 2)
    for i in range(0, maxSizeOfList):
        collectionsOfOddNo.append((2 * i) + 1)

print(collectionsOfOddNo)

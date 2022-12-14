def fib():
    a, b = 0, 1
    while True:
        yield a  # just like return but doesn't eliminate whole code(next will go to for loop then executes next line)
        a, b = b, a + b


for f in fib():
    if f > 13:
        break
    print(f)

# Playing with files

# f = open('Readme.txt')

# readline() function reads files sentences one by one

# data = f.readline()
# print(data)
#
# data = f.readline()
# print(data)
#
# data = f.readline()
# print(data)

# Whereas read() function reads everything which is in the file

# data = f.read()
# print(data)

f = open('sample.txt', 'w')
f.write("Was I able to open new text file and write it?")


f.close()

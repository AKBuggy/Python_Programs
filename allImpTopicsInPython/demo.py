# lambda program
numbers = (4, 7, 19, 2, 89, 45, 72, 22)
sorted_numbers = sorted(numbers)
even = lambda a: a % 2 == 0
even_numbers = list(filter(even, sorted_numbers))
print(type(even_numbers))
print(even_numbers)


# format program
def is_even(number):
    message = f"{number} is an even number" if number % 2 == 0 else f"{number} is an odd number"
    return message


print(is_even(54))

# dictionary comprehension
a = {'Hello': 'World', 'First': 1}
b = {val: k for k, val in a.items()}
b = {val: v for (val, v) in a.items()}
print(b)


# We pass a variable number of arguments into the function using *args, and then print their value.
def tester(*argv):
    print(type(argv))
    print(argv)
    for arg in argv:
        print(arg, end=' ')


tester('Sunday', 'Monday', 'Tuesday', 'Wednesday')

def tester(**kwargs):
    print(type(kwargs))
    print(*kwargs)
    for key, value in kwargs.items():
        print(key, value, end=" ")


tester(Sunday=1, Monday=2, Tuesday=3, Wednesday=4)

a = [[], "abc", [0], 1, 0]
print(list(filter(bool, a)))

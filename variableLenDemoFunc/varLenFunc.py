def add(a, *b):
    sum = a

    for i in b:
        sum = sum + i

    print(sum)


add(5, 6, 34, 78)


def add_elements_as_per_input(*userInput):
    add = 0
    for j in userInput:
        add = add + j

    print(add)


add_elements_as_per_input(5, 4, 4, 1)


def person(name, **data):
    print(name)

    for i, j in data.items():
        print(i, j)


person('Ankit', age=20, city='Mumbai', mob=9321553724)



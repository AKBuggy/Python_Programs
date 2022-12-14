def reverse(data):
    for i in range(len(data) - 1, -1, -1):
        yield data[i]


# data = ['golf', 'cricket', 'football']   # when the data assigned is a list its length is the number of element
data = 'cricket'  # when the data assigned is just one string then its length is the number of character
print(len(data))

for char in reverse(data):
    print(char)






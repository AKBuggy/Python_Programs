'''
names = ["John", "James", "Emmy", "Michael", "Jimmy"]
starts_with_j = [n for n in names if n[0] == "J"]
print(starts_with_j)
'''

# animals = ['lion', 'tiger', 'monkey', 'elephant', 'frog']
# titled_animals = [a.title() for a in animals]
# print(titled_animals)


# numbers = [1, 2, 3, 4, 5]
#
# squared_numbers = [n ** 2 for n in numbers]
# print(squared_numbers)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [n for n in numbers if n % 2 == 0]
# print(even_numbers)


# numbers = [1, 2, 3, 4]
# letters = ['a', 'b', 'c', 'd']
#
# combined = [(numbers[i], letters[i]) for i in range(len(numbers))]
# print(combined)


list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = []
for sublist in list_of_lists:
    for item in sublist:
        flattened_list.append(item)

flattened_list = [item for sublist in list_of_lists for item in sublist]
print(flattened_list)
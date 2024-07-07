def print_pattern(rows):
    start_value = 31
    for i in range(rows, 0, -1):
        print(" " * (rows - i), end="")
        for j in range(i * 2 - 1):
            print(start_value, end=" ")
            start_value -= 2
        print()


# Accept the number of rows as input
rows = int(input("Enter the number of rows for the pattern: "))
print_pattern(rows)

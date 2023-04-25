def get_count_of_binary_sequence(num, seq):  # should return int count
    binary_value = bin(num)[2:]  # slicing because start 2 binary values not required ex: 7 = 0b111
    count = 0  # to count the occurrence
    print(bin(0))
    i = 0
    while i < len(binary_value):
        if binary_value[i:i + len(seq)] == seq:
            count += 1
            i += len(seq) - 1
        else:
            i += 1
    return count


def main():
    inp_num = int(input("Enter an integer number: "))
    sequence = input("Enter a binary sequence: ")

    get_count = get_count_of_binary_sequence(inp_num, sequence)
    print(f"Repeated {get_count} times")


if __name__ == '__main__':
    main()

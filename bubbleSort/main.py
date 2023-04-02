import BubbleSort as bubS


def main():
    t = int(input("How many test cases: "))
    while t:
        inp_len = int(input("Enter the length of the list: "))
        inp_list = []
        for i in range(inp_len):
            val = int(input(f"Enter the values {i + 1}: "))
            inp_list.append(val)

        call_sort = bubS.BubbleSort()
        print_sorted_arr = call_sort.sort(inp_list)
        print(f"Sorted List = {print_sorted_arr}")
        t -= 1


if __name__ == '__main__':
    main()

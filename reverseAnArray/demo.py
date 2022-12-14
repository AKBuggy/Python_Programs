def reverseArray(lst):
    start_index = 0
    end_index = len(lst)-1

    while end_index > start_index:
        lst[start_index], lst[end_index] = lst[end_index], lst[start_index]
        start_index += 1
        end_index -= 1


def main():

    # for multiple testcases
    T = int(input("Enter how many testcases: "))

    while T > 0:
        # lst = []
        # size = int(input("Enter no. of element: "))
        #
        # print("Enter elements: ")
        # for i in range(size):
        #     # ele = list(map(int, input().strip().split()))
        #     ele = int(input())
        #     lst.append(ele)
        lst = [int(x) for x in input().strip().split()]

        reverseArray(lst)
        print(lst)

        T -= 1


if __name__ == '__main__':
    main()


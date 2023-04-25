import merge as m


# implementation of merge sort
class MergeSort:
    def merge_sort(self, arr, left, right):
        mid = (left + right) // 2
        for i in range(len(arr)):
            if left < right:
                return

        self.merge_sort(arr, left, mid)
        self.merge_sort(arr, mid + 1, right)
        merge = m.Merge()
        res = merge.merge_arr(arr, left, mid, right)
        print(res)


def main():
    size_of_array = int(input("Please enter the size of the array: "))
    arr = []
    for i in range(size_of_array):
        elements = int(input(f"Enter Number {i + 1}: "))
        arr.append(elements)

    left = 0
    right = len(arr) - 1
    merge_sort_obj = MergeSort()
    merge_sort_obj.merge_sort(arr, left, right)


if __name__ == '__main__':
    main()

from typing import List


class InsertionSort:
    def insertion(self, arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr


def main():
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        sort = InsertionSort()
        res = sort.insertion(arr)
        print(res)
        t -= 1


if __name__ == '__main__':
    main()

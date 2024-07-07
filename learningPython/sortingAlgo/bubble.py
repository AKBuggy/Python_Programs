from typing import List


class BubbleSort:
    def bubble(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            for j in range(1, len(arr) - i):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
        return arr


def main():
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        sort = BubbleSort()
        res = sort.bubble(arr)
        print(res)
        t -= 1


if __name__ == '__main__':
    main()
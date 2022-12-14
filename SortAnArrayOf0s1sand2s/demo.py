
class Solution:
    def sort012(self, arr):
        low = 0
        mid = 0
        high = len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                mid += 1
                low += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1


def main():
    t = int(input())
    for _ in range(t):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sort012(arr)
        for i in arr:
            print(i, end=' ')
        print()


if __name__ == '__main__':
    main()


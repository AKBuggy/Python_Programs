class Solution:
    def partition(self, arr, left, right):
        yellow = left + 1
        for green in range(left + 1, right):
            if arr[green] <= arr[left]:
                arr[yellow], arr[green] = arr[green], arr[yellow]
                yellow += 1

        arr[left], arr[yellow - 1] = arr[yellow - 1], arr[left]
        return yellow - 1

    def quickSort(self, arr, left, right):
        # if right - left <= 1: return
        if left < right:
            idx = self.partition(arr, left, right)
            left_inversions = self.quickSort(arr, left, idx)
            right_inversions = self.quickSort(arr, idx + 1, right)
            return left_inversions + right_inversions + idx - left
        else:
            return 0

    def print_arr(self, arr, n):
        for i in range(n):
            print(arr[i], end=" ")
        print()


if __name__ == '__main__':
    size = int(input("Enter the size of the array: "))
    arr = list(map(int, input("Enter the elements of the array: ").split(" ")))

    quick = Solution()
    inversions = quick.quickSort(arr, 0, size)
    quick.print_arr(arr, size)
    print(inversions)



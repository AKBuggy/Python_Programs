from typing import List


class Merge:
    def merge(self, nums: List[int], l: int, r: int, m: int) -> List[int]:
        n1 = m - l + 1
        n2 = r - m

        L = nums[l: m + 1]
        R = nums[m + 1:]

        i, j, k = 0, 0, l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            nums[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            nums[k] = R[j]
            j += 1
            k += 1

        return nums

    def mergeSort(self, nums: List[int], l: int, r: int) -> List[int]:
        if l < r:
            m = (l + r) // 2

            self.mergeSort(nums, l, m)
            self.mergeSort(nums, m + 1, r)
            self.merge(nums, l, r, m)

        return nums


def main():
    t = int(input())
    while t > 0:
        nums = list(map(int, input().split()))
        sort = Merge()
        res = sort.mergeSort(nums, 0, (len(nums) - 1))
        print(res)
        t -= 1


if __name__ == '__main__':
    main()

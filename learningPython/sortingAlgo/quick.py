# imp point
# - pivot
# - yellow, green pointer
# swapping yellow's element and green's element if pivot is greater than curr element
# else incrementing green pointer

class Quick:
    def quick_sort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            pivot = nums[0]
            left = [x for x in nums[1:] if x < pivot]
            right = [x for x in nums[1:] if x >= pivot]
            return self.quick_sort(left) + [pivot] + self.quick_sort(right)


def main():
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        sort = Quick()
        print(sort.quick_sort(arr))
        t -= 1


if __name__ == '__main__':
    main()

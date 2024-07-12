class Selection:
    def selection_sort(self, nums):
        for i in range(len(nums)):
            min_ele_idx = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_ele_idx]:
                    min_ele_idx = j
            nums[i], nums[min_ele_idx] = nums[min_ele_idx], nums[i]

        return nums


def main():
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        sort = Selection()
        print(sort.selection_sort(arr))
        t -= 1


if __name__ == '__main__':
    main()

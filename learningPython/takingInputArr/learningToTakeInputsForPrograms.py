from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2: return slow


# driver code
def main():
    t = int(input("test cases: "))
    while t > 0:
        nums = list(map(int, input("space separated array: ").split()))
        obj = Solution()
        print(obj.findDuplicate(nums))
        t -= 1


if __name__ == '__main__':
    main()

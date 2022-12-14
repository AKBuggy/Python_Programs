# grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
# i=0
# j=0
# print(len(grid))

import re


# class Solution:
#     # @param A : string
#     # @return an long
#     def solve(self, a: str) -> int:
#         sum = 0
#         numbers = re.findall(r'\d+', a)
#         print(numbers)
#         for i in numbers:
#             sum += int(i)
#         return sum
#
#
# if __name__ == '__main__':
#     # a = "a12b34c"
#     a = "124"
#     obj = Solution()
#     res = obj.solve(a)
#     print(res)

# class Solution:
#     # @param A : string
#     # @return an integer
#     def solve(self, A):
#         count = 0
#         splitTheSentence = A.split()
#         for i in range(0, len(splitTheSentence)):
#             res = splitTheSentence[i].reverse()
#             if (splitTheSentence[i] == res):
#                 count += 1
#         return count

class Solution:
    def maxPower(self, s: str) -> int:
        element = s[0]
        current_count = 1
        max_count = 0

        for i in range(1, len(s)):
            if element == s[i]:
                current_count += 1
            else:
                max_count = max(current_count, max_count)
                element = s[i]
                current_count = 1
        return max_count



if __name__ == '__main__':
    A = "abbcccddddeeeeedcba"
    obj = Solution()
    res = obj.maxPower(A)
    print(res)

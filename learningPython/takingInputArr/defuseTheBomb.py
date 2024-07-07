from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        decrypt = [0] * len(code)
        if k > 0:
            r = 1
            curr_sum = 0
            while k > 0:
                curr_sum += code[r]
                r += 1
                k -= 1
            decrypt[0] = curr_sum
            l = 1
            while l < len(code):
                curr_sum = curr_sum - code[l] + code[r % len(code)]
                decrypt[l] = curr_sum
                l += 1
                r += 1
        elif k < 0:
            l = len(code) - 2
            curr_sum = 0
            while k < 0:
                curr_sum += code[l]
                l -= 1
                k += 1
            decrypt[len(code) - 1] = curr_sum
            r = len(code) - 2
            while r > -1:
                curr_sum = curr_sum - code[r] + code[l]
                decrypt[r] = curr_sum
                r -= 1
                l -= 1
        else:
            return [0] * len(code)

        return decrypt


def main():
    t = int(input())
    while t > 0:
        code = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        res = obj.decrypt(code, k)

        print(res)


if __name__ == '__main__':
    main()

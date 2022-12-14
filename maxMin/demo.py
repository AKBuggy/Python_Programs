import sys


def getMinMax(a):
    # MAX = sys.maxsize
    # MIN = -sys.maxsize - 1
    MAX = float('-inf')
    MIN = float('inf')

    for ele in a:
        if ele < MIN:
            MIN = ele
        if ele > MAX:
            MAX = ele

    return MIN, MAX


# {
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while T > 0:
        # n = int(input())
        a = [int(x) for x in input().strip().split()]

        product = getMinMax(a)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
# if __name__ == '__main__':
#     a = [1, 1, 30, 1]
#     print(getMaxMin(a))


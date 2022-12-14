import sys


def Solve(N, A):
    # Write your code here
    A.sort()
    close = sys.maxsize

    for i in range(len(A)):
        if abs(A[i] <= close):
            close = abs(A[i])
            ans = A[i]

    return ans


N = input()
A = list(map(int, input().split()))
out_ = Solve(N, A)
print(out_)
def count_good_subsequences(A, K):
    MOD = 10 ** 9 + 7
    N = len(A)
    DP = [[0] * (K + 2) for _ in range(N)]

    for i in range(N):
        DP[i][1] = 1

    for i in range(N):
        for k in range(2, K + 2):
            for j in range(i):
                if A[j] < A[i]:
                    DP[i][k] = (DP[i][k] + DP[j][k - 1]) % MOD

    result = 0
    for i in range(N):
        result = (result + DP[i][K + 1]) % MOD

    return result


A = [5, 6, 1, 3, 4]
K = 2
print(count_good_subsequences(A, K))

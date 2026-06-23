def solution():
    n = int(input())
    a = list(map(int, input().split()))

    memo = [[-1] * n for _ in range(n)]

    def dp(i, j):
        if i >= j: return 0
        if memo[i][j] > -1: return memo[i][j]
        ret = (1 if a[i] == a[j] else 0)+dp(i+1,j-1)
        for k in range(i+1, j-1, 2):
            ret = max(ret, dp(i,k)+dp(k+1,j))
        memo[i][j] = ret
        return ret

    res = dp(0, n-1)
    a = a[1:]+[a[0]]
    memo = [[-1] * n for _ in range(n)]
    res = max(res, dp(0, n-1))

    print(res)
solution()
def solution():
    s = input().strip()
    n = len(s)

    memo = [[-1] * n for _ in range(n)]

    def dp(i, j):
        if i >= j: return 0
        elif memo[i][j] > -1: return memo[i][j]

        ret = (1 if s[i]+s[j] in ('at', 'gc') else 0) + dp(i+1, j-1)
        for k in range(i, j):
            ret = max(ret, dp(i,k)+dp(k+1,j))
        memo[i][j] = ret

        return ret

    res = dp(0, n-1)
    print(res*2)
solution()
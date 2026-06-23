def solution():
    mod = 1_000_000_003
    n = int(input())
    k = int(input())

    res = 0

    dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n)]
    dp[0][1][1] = 1

    for i in range(1, n):
        for j in range(min(i, k)+1):
            dp[i][j][0] = (dp[i-1][j][1]+dp[i-1][j][0])%mod
            if j > 0: dp[i][j][1] = dp[i-1][j-1][0]
    res += dp[-1][k][0]

    dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n)]
    dp[0][0][0] = 1

    for i in range(1, n):
        for j in range(min(i, k)+1):
            dp[i][j][0] = (dp[i-1][j][1]+dp[i-1][j][0])%mod
            if j > 0: dp[i][j][1] = dp[i-1][j-1][0]
    res += dp[-1][k][0]+dp[-1][k][1]

    res %= mod

    print(res)
solution()
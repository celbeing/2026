def solution():
    n, m = map(int, input().split())
    a = set()
    if m: a.update(map(int, input().split()))
    INF = float('inf')
    dp = [[INF] * 41 for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(1, n+1):
        for j in range(41):
            dp[i][j] = dp[i-1][j] + (0 if i in a else 10000)
            if i >= 3 and 40 > j > 0:
                dp[i][j] = min(dp[i][j], dp[i-3][j-1] + 25000)
            if i >= 5 and 39 > j > 1:
                dp[i][j] = min(dp[i][j], dp[i-5][j-2] + 37000)
            if 38 > j:
                dp[i][j] = min(dp[i][j], dp[i-1][j+3])
    print(min(dp[n]))
solution()
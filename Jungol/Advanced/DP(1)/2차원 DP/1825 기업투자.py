def solution():
    n, m = map(int, input().split())
    reward = [[0] * (n+1) for _ in range(m)]
    for j in range(1, n+1):
        a = list(map(int, input().split()))[1:]
        for i in range(m):
            reward[i][j] = a[i]
    dp = [[0] * (n+1) for _ in range(m)]
    route = [[0] * (n+1) for _ in range(m)]
    for i in range(1, n+1):
        dp[0][i] = reward[0][i]
        route[0][i] = i

    for i in range(1, m):
        for j in range(1, n+1):
            for k in range(j+1):
                if dp[i][j] < dp[i-1][j-k]+reward[i][k]:
                    dp[i][j] = dp[i-1][j-k]+reward[i][k]
                    route[i][j] = k
    print(dp[m-1][n])
    res = []
    for i in range(m-1, -1, -1):
        res.append(route[i][n])
        n -= res[-1]
    res.reverse()
    print(*res)
solution()
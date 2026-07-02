def solution():
    INF = -float('inf')
    d = [(1,0), (0, 1), (0,-1)]
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    dp = [[INF]*n for _ in range(n)]
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[0][i] = dp[0][i-1]+grid[0][i]
    for i in range(1, n):
        r = [INF]*n
        l = [INF]*n
        r[0] = dp[i-1][0]+grid[i][0]
        for j in range(1, n):
            r[j] = max(dp[i-1][j], r[j-1])+grid[i][j]
        l[n-1] = dp[i-1][-1]+grid[i][-1]
        for j in range(n-2, -1, -1):
            l[j] = max(dp[i-1][j], l[j+1])+grid[i][j]
        for j in range(n):
            dp[i][j] = max(l[j], r[j])
    print(dp[n-1][n-1])
solution()
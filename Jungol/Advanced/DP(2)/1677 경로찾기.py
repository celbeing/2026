def solution():
    INF = -float('inf')
    d = [(1,0), (0, 1), (0,-1)]
    n = int(input())
    grid = [list(map(int, input().split())) + [0] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            grid[i][j] += grid[i][j-1]

    dp = [[INF]*n for _ in range(n)]
    for i in range(n):
        dp[0][i] = grid[0][i]
    for i in range(1, n):
        for j in range(n):
            for k in range(j+1):
                dp[i][j] = max(dp[i][j], dp[i-1][k]+grid[i][j]-grid[i][k-1])
            for k in range(j+1, n):
                dp[i][j] = max(dp[i][j], dp[i-1][k]+grid[i][k]-grid[i][j-1])
    print(dp[n-1][n-1])
solution()
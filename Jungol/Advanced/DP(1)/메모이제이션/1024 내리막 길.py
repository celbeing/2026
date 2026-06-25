def solution():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    height = []
    for i in range(n):
        for j in range(m):
            height.append((-grid[i][j], i, j))
    height.sort()

    d = [(1,0),(0,1),(-1,0),(0,-1)]
    for h, x, y in height:
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and grid[x][y] < grid[nx][ny]:
                dp[x][y] += dp[nx][ny]

    print(dp[-1][-1])
solution()
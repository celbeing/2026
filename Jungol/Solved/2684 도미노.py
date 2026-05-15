import sys
input = sys.stdin.readline

def solution():
    INF = -float('inf')
    n, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[INF] * 8 for _ in range(k+1)] for _ in range(n)]
    dp[0][0][0] = 0
    for i in range(n-1):
        dp[i+1][k][0] = max(dp[i][k])
        # 000
        for j in range(k):
            dp[i+1][j][0] = max(max(dp[i][j]), dp[i+1][j][0])
            dp[i+1][j+1][0] = max(dp[i][j][0] + grid[i][0]+grid[i][1],
                                  dp[i][j][0] + grid[i][1]+grid[i][2],
                                  dp[i][j][1] + grid[i][0]+grid[i][1],
                                  dp[i][j][4] + grid[i][1]+grid[i][2],
                                  dp[i+1][j+1][0])

        # 001
        for j in range(k):
            dp[i+1][j+1][1] = max(dp[i][j][0] + grid[i][2]+grid[i+1][2],
                                  dp[i][j][4] + grid[i][2]+grid[i+1][2],
                                  dp[i][j][2] + grid[i][2]+grid[i+1][2],
                                  dp[i][j][6] + grid[i][2]+grid[i+1][2],
                                  dp[i+1][j+1][1])
            if j < k-1:
                dp[i+1][j+2][1] = max(dp[i][j][0] + grid[i][0]+grid[i][1]+grid[i][2]+grid[i+1][2],
                                      dp[i+1][j+2][1])

        # 010
        for j in range(k):
            dp[i+1][j+1][2] = max(dp[i][j][0] + grid[i][1]+grid[i+1][1],
                                  dp[i][j][1] + grid[i][1]+grid[i+1][1],
                                  dp[i][j][4] + grid[i][1]+grid[i+1][1],
                                  dp[i][j][5] + grid[i][1]+grid[i+1][1],
                                  dp[i+1][j+1][2])

        # 100
        for j in range(k):
            dp[i+1][j+1][4] = max(dp[i][j][0] + grid[i][0]+grid[i+1][0],
                                  dp[i][j][1] + grid[i][0]+grid[i+1][0],
                                  dp[i][j][2] + grid[i][0]+grid[i+1][0],
                                  dp[i][j][3] + grid[i][0]+grid[i+1][0],
                                  dp[i+1][j+1][4])
            if j < k-1:
                dp[i+1][j+2][4] = max(dp[i][j][0] + grid[i][0]+grid[i][1]+grid[i][2]+grid[i+1][0],
                                      dp[i+1][j+2][4])

        # 011
        for j in range(k-1):
            dp[i+1][j+2][3] = max(dp[i][j][0] + grid[i][1]+grid[i][2]+grid[i+1][1]+grid[i+1][2],
                                  dp[i][j][4] + grid[i][1]+grid[i][2]+grid[i+1][1]+grid[i+1][2],
                                  dp[i+1][j+2][3])

        # 101
        for j in range(k-1):
            dp[i+1][j+2][5] = max(dp[i][j][0] + grid[i][0]+grid[i][2]+grid[i+1][0]+grid[i+1][2],
                                  dp[i][j][2] + grid[i][0]+grid[i][2]+grid[i+1][0]+grid[i+1][2],
                                  dp[i+1][j+2][5])

        # 110
        for j in range(k-1):
            dp[i+1][j+2][6] = max(dp[i][j][0] + grid[i][0]+grid[i][1]+grid[i+1][0]+grid[i+1][1],
                                  dp[i][j][1] + grid[i][0]+grid[i][1]+grid[i+1][0]+grid[i+1][1],
                                  dp[i+1][j+2][6])
        # 111
        for j in range(k-2):
            dp[i+1][j+3][7] = max(dp[i][j][0] + sum(grid[i])+sum(grid[i+1]),
                                  dp[i+1][j+3][7])

    result = max(dp[-1][k-1][0] + grid[-1][0]+grid[-1][1],
                 dp[-1][k-1][0] + grid[-1][1]+grid[-1][2],
                 dp[-1][k-1][1] + grid[-1][0]+grid[-1][1],
                 dp[-1][k-1][4] + grid[-1][1]+grid[-1][2],
                 max(dp[-1][k]))
    print(result)
solution()
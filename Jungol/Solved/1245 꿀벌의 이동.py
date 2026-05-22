n = int(input())
d = [(-1,-1),(-1,0),(0,-1),(0,1),(1,0),(1,1)]
dp = [[[0] * 42 for _ in range(42)] for _ in range(21)]
dp[0][0][0] = 1
for i in range(n):
    for x in range(-20,21):
        for y in range(-20,21):
            if dp[i][x][y] == 0: continue

            for dx, dy in d:
                dp[i+1][x+dx][y+dy] += dp[i][x][y]
print(dp[n][0][0])
n, l = map(int, input().split())
total = sum(list(map(int, input().split())))
dp = [[[0] * (n+1) for _ in range(n*2+1)] for _ in range(n*2+1)]
# dp[i][j][k] = i번째 카드 깠을 때, j번 틀리고 위치 아는 카드 k장
dp[0][0][0] = 1
dp[1][0][1] = 1

for i in range(2, n*2+1):
    for j in range(1, n*2+1):
        dp[i][j][0] += dp[i-1][j][0]
        for k in range(1, n+1):
            dp[i][j][k] += dp[i-1][j][k] + dp[i-2][j-1][k-1] + dp[i-2][j][k-1]
            if k > 1:
                dp[i][j][k] += dp[i-2][j-1][k-2]

case = 0
score = 0
for i in range(n*2+1):
    if i < l:
        score += dp[n*2][i][n]
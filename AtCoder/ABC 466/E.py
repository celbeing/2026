N, K = map(int, input().split())
INF = -float('inf')
dp = [[[INF]*2 for _ in range(K+1)] for _ in range(N+1)]
dp[0][0][0] = 0

card = [0]
res = 0
for _ in range(N):
    a, b = map(int, input().split())
    card.append(b-a)
    res += a

for i in range(1, N+1):
    dp[i][0][0] = 0
    for k in range(1, K+1):
        dp[i][k][0] = max(dp[i-1][k])
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]) + card[i]

m = INF
for i in range(0, K+1):
    m = max(m, max(dp[N][i]))
res += m
print(res)
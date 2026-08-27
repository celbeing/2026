def solution():
    n = int(input())
    a = list(map(int, input().split()))

    cost = [[0] * n for _ in range(n)]
    for s in range(n):
        if a[s]: cost[s][s] = 1
        i = 1
        for e in range(s+1, n):
            cost[s][e] = cost[s][e-1] + (1 if a[e] != i else 0)

            i += 1

    dp = [[n] * n for _ in range(n)]
    for i in range(n):
        dp[i][0] = cost[0][i]
        for j in range(1, i+1):
            for k in range(j, i+1):
                dp[i][j] = min(dp[k-1][j-1]+cost[k][i], dp[i][j])

    for i in range(n):
        print(dp[-1][i])

solution()
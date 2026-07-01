def solution():
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    for i in range(1, n):
        a[i] += a[i-1]
    for i in range(n-1, k-1, -1):
        a[i] -= a[i-k]
    dp = [[0] * 4 for _ in range(n)]

    for i in range(k-1, n):
        for j in range(1, 4):
            dp[i][j] = max(dp[i][j], dp[i-k][j-1] + a[i], dp[i-1][j])
    print(dp[n-1][3])
solution()
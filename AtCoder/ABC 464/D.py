def solution():
    n = int(input())
    s = input().strip()
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    dp = [[0] * 2 for _ in range(n)]
    if s[0] == 'S':
        dp[0][1] = -x[0]
    else:
        dp[0][0] = -x[0]

    for i in range(1, n):
        if s[i] == 'S':
            dp[i][0] = max(dp[i-1][1]+y[i-1], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0]-x[i], dp[i-1][1]-x[i])
        else:
            dp[i][0] = max(dp[i-1][0]-x[i], dp[i-1][1]-x[i]+y[i-1])
            dp[i][1] = max(dp[i-1][0], dp[i-1][1])
    print(max(dp[-1][0], dp[-1][1]))
for _ in range(int(input())):
    solution()
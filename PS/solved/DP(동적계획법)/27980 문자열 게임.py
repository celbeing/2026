def solution():
    n, m = map(int, input().split())
    board = list(input().strip())
    string = list(input().strip())
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        if board[i] == string[0]:
            dp[i][0] = 1
    for j in range(1, m):
        if board[0] == string[j]: dp[0][j] = dp[1][j - 1] + 1
        else: dp[0][j] = dp[1][j - 1]
        for k in range(1, n - 1):
            dp[k][j] = max(dp[k - 1][j - 1], dp[k + 1][j - 1])
            if board[k] == string[j]: dp[k][j] += 1
        if board[-1] == string[j]: dp[-1][j] = dp[-2][j - 1] + 1
        else: dp[-1][j] = dp[-2][j - 1]

    res = 0
    for i in range(n):
        res = max(res, dp[i][-1])
    print(res)

solution()
def solution():
    scroll = input().strip()
    demon, angel = input().strip(), input().strip()
    n = len(scroll)
    m = len(angel)
    dp = [[0]*(n+1) for _ in range(2)]
    dp[0][-1] = dp[1][-1] = 1
    for i in range(m):
        d, a = demon[i], angel[i]
        for j in range(n-1,-1,-1):
            s = scroll[j]
            if d == s:
                dp[0][j] += dp[1][j-1]
            if a == s:
                dp[1][j] += dp[0][j-1]
    print(dp[0][-2]+dp[1][-2])
solution()
def solution():
    n = int(input())
    a = list(map(int, list(input().strip())))
    b = input().strip()+'*#'
    a[-1] += 1
    dp = [[0] * 8 for _ in range(n+1)]
    dp[-1][1] = 1
    for i in range(n):
        if a[i] == 0:
            dp[i][0] = max(dp[i-1][0], dp[i-1][4])
        elif a[i] == 1:
            dp[i][1] = max(dp[i-1][0], dp[i-1][4])+1
            if b[i+1] == '#':
                dp[i][2] = max(dp[i-1][1], dp[i-1][5])
                dp[i][4] = max(dp[i-1][2], dp[i-1][6])
        elif a[i] == 2:
            dp[i][3] = max(dp[i-1][1], dp[i-1][5])+1
            dp[i][5] = max(dp[i-1][2], dp[i-1][6])+1
            if b[i+1] == '#': dp[i][6] = max(dp[i-1][3], dp[i-1][7])
        else:
            dp[i][7] = max(dp[i-1][3], dp[i-1][7])+1
    print(max(dp[n-1])-1)
solution()
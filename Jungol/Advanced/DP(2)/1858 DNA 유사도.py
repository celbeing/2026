def solution():
    n = int(input())
    a = ' '+input().strip()
    m = int(input())
    b = ' '+input().strip()
    dp = [[0] * (m+1) for _ in range(n+1)]
    tr = [[(i, j) for j in range(m+1)] for i in range(n+1)]

    result = 0
    s, e = (0, 0), (0, 0)

    for i in range(1, n+1):
        for j in range(1, m+1):
            d = 3 if a[i] == b[j] else -2

            if dp[i][j] < dp[i-1][j-1]+d:
                dp[i][j] = dp[i-1][j-1]+d
                tr[i][j] = tr[i-1][j-1]

            if dp[i][j] < dp[i-1][j]-2:
                dp[i][j] = dp[i-1][j]-2
                tr[i][j] = tr[i-1][j]

            if dp[i][j] < dp[i][j-1]-2:
                dp[i][j] = dp[i][j-1]-2
                tr[i][j] = tr[i][j-1]

            if result < dp[i][j]:
                result = dp[i][j]
                s = tr[i][j]
                e = (i, j)
    print(result)
    print(a[s[0]+1:e[0]+1])
    print(b[s[1]+1:e[1]+1])
solution()
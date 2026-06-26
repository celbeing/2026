def solution():
    n, m = map(int, input().split())
    dp = [0] * (m+1)
    for i in range(1, n+1):
        w, c, k = map(int, input().split())
        bit = 1
        while k:
            if bit > k: bit = k
            nc, nw = c*bit, w*bit
            k -= bit
            bit <<= 1
            if nw > m: continue

            for j in range(m, nw-1, -1):
                dp[j] = max(dp[j-nw]+nc, dp[j])

    print(dp[m])

solution()
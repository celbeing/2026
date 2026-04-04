import sys
input = sys.stdin.readline

s = input().strip()
t = ' '+input().strip()
n = len(t)-1

dp = [0] * n
res = 0

for i in s:
    for j in range(n-1,0,-1):
        now = 0
        if i == t[j+1]:
            dp[j] = 0
        if i == t[j]:
            dp[j] += dp[j-1]
        if j == 1 and i == t[1]:
            dp[j] += 1
        res += dp[j]
    if i == t[1]:
        dp[0] = 0
    else:
        dp[0] += 1
    res += dp[0]

print(res)
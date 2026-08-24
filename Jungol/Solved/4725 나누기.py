n = int(input())
a = list(map(int, input().split()))
p = [0] * n
for i in range(n):
    p[i] = p[i-1]+a[i]

if p[-1] % 4:
    print(0)
elif p[-1] == 0:
    cnt = p.count(0)-1
    res = cnt*(cnt-1)*(cnt-2)
    res //= 6
    print(res)
else:
    t = p[-1]//4
    dp = [0]*4
    for i in range(n):
        if p[i] == t*3:
            dp[3] += dp[2]
        if p[i] == t*2:
            dp[2] += dp[1]
        if p[i] == t:
            dp[1] += 1
    print(dp[3])
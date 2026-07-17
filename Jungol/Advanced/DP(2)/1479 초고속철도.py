# 선택하지 않는 구간에 대한 문제로 변형
from bisect import bisect_left

def solution():
    mod = 20070713

    n = int(input())
    bot = [tuple(map(int, input().split())) for _ in range(n)]
    bot.sort(key=lambda x:x[1])
    right = [r for l, r in bot]

    dp = [0] * n
    pre = [0] * (n+1)
    for i, (l, r) in enumerate(bot):
        bef = bisect_left(right, l)
        dp[i] = 1 + pre[bef]
        pre[i+1] = (pre[i]+dp[i])%mod
    print(1+pre[n])
solution()
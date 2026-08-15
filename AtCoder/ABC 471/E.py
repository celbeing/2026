import sys
input = sys.stdin.readline
from math import comb

mod = 998244353
n, k = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)%mod

sq = 0
for t in a:
    sq += t * t
    sq %= mod
res = sq*(comb(n - 1, k - 1) % mod)
res %= mod

if k > 1:
    c = comb(n - 2, k - 2) % mod
    cross = (s*s-sq)%mod
    res += cross*c
    res %= mod

print(res)
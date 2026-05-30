import sys
from math import gcd
input = sys.stdin.readline
mod = 998244353
def solution():
    n, m = map(int, input().split())
    res = 0
    digit = 1
    for d in range(1, 20):
        s, e = digit, digit*10-1
        if n < s: break

        y = min(n,e)-s+1
        x = n // (m // gcd(m,e))
        res += (y%mod)*(x%mod)
        res %= mod
        digit *= 10
    print(res)
for _ in range(int(input())):
    solution()
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] %= k
a.sort()
res = a[-1] - a[0]
for i in range(n - 1):
    t = a[i] + k - a[i + 1]
    if res > t:
        res = t
print(res)
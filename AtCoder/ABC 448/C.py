import sys
input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))
d = dict()
for i in range(n):
    a[i] = (a[i], i + 1)
    d[i + 1] = a[i][0]
a.sort()
lim = min(6, len(a))
small = []
for i in range(lim):
    small.append(a[i][1])
for _ in range(q):
    k = int(input())
    b = set(map(int, input().split()))
    for s in small:
        if not(s in b):
            print(d[s])
            break
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
c = list(map(int, input().split()))
pepper = 0
for _ in range(n):
    a, b = map(int, input().split())
    pepper += min(c[a - 1], b)
    c[a - 1] -= min(c[a - 1], b)
print(pepper)
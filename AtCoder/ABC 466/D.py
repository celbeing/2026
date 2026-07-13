n, m = map(int, input().split())
dots = [tuple(map(int, input().split())) for _ in range(m)]
r = [0] * (n+1)
c = [0] * (n+1)
res = 0
for a, b in reversed(dots):
    if r[a] == 0 and c[b] == 0:
        res += 1
    r[a] = 1
    c[b] = 1
print(res)
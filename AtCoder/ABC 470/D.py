n, q = map(int, input().split())
p = [[0] * (n + 1) for _ in range(2)]
P = list(map(int, input().split()))
for i, PP in enumerate(P, start=1):
    p[0][i] = PP
    p[1][PP] = i

swt = 0
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a, b = query[1:]
        p[swt^1][p[swt][a]], p[swt^1][p[swt][b]] = p[swt^1][p[swt][b]], p[swt^1][p[swt][a]]
        p[swt][a], p[swt][b] = p[swt][b], p[swt][a]
    else:
        swt ^= 1
print(*p[swt][1:])
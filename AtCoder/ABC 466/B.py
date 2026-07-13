n, m = map(int, input().split())
colors = [-1] * (m+1)
for _ in range(n):
    c, s = map(int, input().split())
    colors[c] = max(colors[c], s)
print(*colors[1:])
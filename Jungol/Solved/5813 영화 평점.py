INF = float('inf')
n, m = map(int, input().split())
a = list(map(int, input().split()))
size = 1
while size < m:
    size <<= 1
seg = [INF] * size * 2

res = []
k = 0
for p in a:
    if k == m: k = 0
    idx = k + size
    seg[idx] = p
    idx >>= 1
    while idx:
        seg[idx] = min(seg[idx*2], seg[idx*2+1])
        idx >>= 1
    res.append(seg[1])
    k += 1
print(*res)
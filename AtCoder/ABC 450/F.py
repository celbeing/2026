mod = 998244353
n, m = map(int, input().split())
link = []
for _ in range(m):
    x, y = map(int, input().split())
    link.append((x, y))
link.sort()

seg = [0] * n * 4
lazy = [0] * n * 4

pow2 = [1] * (m + 1)
for i in range(1, m + 1):
    pow2[i] = pow2[i - 1] * 2
    pow2[i] %= mod

def push(node, start, end):
    if lazy[node] and start < end:
        seg[node * 2] *= pow2[lazy[node]]
        seg[node * 2 + 1] *= pow2[lazy[node]]
        seg[node * 2] %= mod
        seg[node * 2 + 1] %= mod
        lazy[node * 2] += lazy[node]
        lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0
    return

def query(node, start, end, left, right):
    if end < left or right < start: return 0
    if left <= start and end <= right:
        return seg[node]

    push(node, start, end)
    mid = (start + end) // 2
    return (query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)) % mod

def update_mul(node, start, end, left, right):
    if end < left or right < start:
        return

    if left <= start and end <= right:
        seg[node] <<= 1
        seg[node] %= mod
        lazy[node] += 1
        return

    push(node, start, end)
    mid = (start + end) // 2
    update_mul(node * 2, start, mid, left, right)
    update_mul(node * 2 + 1, mid + 1, end, left, right)
    seg[node] = (seg[node * 2] + seg[node * 2 + 1]) % mod
    return

def update(node, start, end, tar, w):
    if start == end:
        seg[node] += w
        seg[node] %= mod
        return

    push(node, start, end)
    mid = (start + end) // 2
    if tar <= mid:
        update(node * 2, start, mid, tar, w)
    else:
        update(node * 2 + 1, mid + 1, end, tar, w)

    seg[node] = (seg[node * 2] + seg[node * 2 + 1]) % mod
    return

update(1, 1, n, 1, 1)

for x, y in link:
    cnt = query(1, 1, n, x, y)
    if y < n: update_mul(1, 1, n, y + 1, n)
    node, start, end = 1, 1, n
    update(1, 1, n, y, cnt)

print(query(1, 1, n, n, n))
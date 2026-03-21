import sys
input = sys.stdin.readline

mod = 998244353
n, m = map(int, input().split())
link = []
for _ in range(m):
    x, y = map(int, input().split())
    link.append((x, y))
link.sort()

seg = [0] * (n + 1) * 8
tag = [0] * (n + 1) * 8
pow2 = [1] * (m + 1)
for i in range(1, m + 1):
    pow2[i] = pow2[i - 1] * 2
    pow2[i] %= mod
tmp = 1
while tmp < len(seg):
    seg[tmp] += 1
    tmp <<= 1



def push(node):
    if tag[node]:
        seg[node * 2] *= pow2[tag[node]]
        seg[node * 2 + 1] *= pow2[tag[node]]
        seg[node * 2] %= mod
        seg[node * 2 + 1] %= mod
        tag[node * 2] += tag[node]
        tag[node * 2 + 1] += tag[node]
    tag[node] = 0

def query_sum(node, start, end, left, right):
    if end < left or right < start: return 0
    push(node)

    if left <= start and end <= right:
        return seg[node]
    mid = (start + end) // 2
    return (query_sum(node * 2, start, mid, left, right) + query_sum(node * 2 + 1, mid + 1, end, left, right)) % mod

def lazy_seg(node, start, end, left, right):
    if end < left or right < start: return
    if left <= start and end <= right:
        seg[node] <<= 1
        seg[node] %= mod
        tag[node] += 1
        return
    mid = (start + end) // 2
    lazy_seg(node * 2, start, mid, left, right)
    lazy_seg(node * 2 + 1, mid + 1, end, left, right)
    seg[node] = seg[node * 2] + seg[node * 2 + 1]
    return

for x, y in link:
    cnt = query_sum(1, 1, n, x, y)
    if y < n: lazy_seg(1, 1, n, y + 1, n)

    node, start, end = 1, 1, n
    while start < end:
        push(node)
        mid = (start + end) // 2
        if y <= mid:
            node *= 2
            end = mid
        else:
            node *= 2
            node += 1
            start = mid + 1

    while node > 0:
        seg[node] += cnt
        node //= 2

print(query_sum(1, 1, n, n, n))
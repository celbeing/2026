import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

size = 1
while size < n:
    size <<= 1

INF = int(1e9)
min_seg = [INF] * size * 2
max_seg = [-INF] * size * 2
inc_seg = [0] * size * 2

for i in range(n):
    min_seg[size+i] = a[i]
    max_seg[size+i] = a[i]

for i in range(size-1,0,-1):
    min_seg[i] = min(min_seg[i*2], min_seg[i*2+1])
    max_seg[i] = max(max_seg[i*2], max_seg[i*2+1])
    inc_seg[i] = max(max(inc_seg[i*2], inc_seg[i*2+1]), max_seg[i*2+1] - min_seg[i*2])

def update(idx, k):
    i = idx+size-1
    min_seg[i] = k
    max_seg[i] = k
    i >>= 1
    while i > 0:
        min_seg[i] = min(min_seg[i*2], min_seg[i*2+1])
        max_seg[i] = max(max_seg[i*2], max_seg[i*2+1])
        inc_seg[i] = max(max(inc_seg[i*2], inc_seg[i*2+1]), max_seg[i*2+1] - min_seg[i*2])
        i >>= 1

def query(l, r):
    l, r = size+l-1, size+r-1
    node = []
    right_node = []

    while l < r:
        if l & 1:
            node.append(l)
            l += 1
        l >>= 1

        if not(r & 1):
            right_node.append(r)
            r -= 1
        r >>= 1
    if l == r:
        node.append(l)
    node += reversed(right_node)

    res = inc_seg[node[0]]
    left_min = min_seg[node[0]]
    if len(node) > 1:
        for i in node[1:]:
            res = max(max(inc_seg[i], max_seg[i] - left_min), res)
            left_min = min(left_min, min_seg[i])
    print(res)

for _ in range(int(input())):
    q, a, b = map(int, input().split())
    if q == 1:
        update(a, b)
    else:
        query(a, b)
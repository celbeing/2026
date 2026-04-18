# python3(with stdin.readline): 2436ms , pypy3: 2156ms
n, m = map(int, input().split())
seg = [0] * n * 4
lazy = [0] * n * 4

def query(node, start, end, left, right):
    push(node, start, end)
    if end < left or right < start:
        return 0

    if left <= start and end <= right:
        return seg[node]
    else:
        mid = (start + end) // 2
        return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

def update(node, start, end, left, right):
    push(node, start, end)
    if end < left or right < start:
        return

    if left <= start and end <= right:
        lazy[node] ^= 1
        push(node, start, end)
        return

    mid = (start + end) // 2
    update(node*2, start, mid, left, right)
    update(node*2+1, mid+1, end, left, right)
    seg[node] = seg[node*2] + seg[node*2+1]
    return

def push(node, start, end):
    if lazy[node]:
        seg[node] = (end - start + 1) - seg[node]
        if start < end:
            lazy[node*2] ^= 1
            lazy[node*2+1] ^= 1
        lazy[node] = 0
    return

for _ in range(m):
    o, s, t = map(int, input().split())
    if o == 1:
        print(query(1, 1, n, s, t))
    else:
        update(1, 1, n, s, t)
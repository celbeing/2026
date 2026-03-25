import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

seg = [0] * n * 4
lazy = [0] * n * 4

def init_tree(node, start, end, left, right, w):
    if end < left or right < start:
        return

    if start == end:
        seg[node] += w
    else:
        mid = (start + end) // 2
        init_tree(node * 2, start, mid, left, right, w)
        init_tree(node * 2 + 1, mid + 1, end, left, right, w)
        seg[node] = seg[node * 2] + seg[node * 2 + 1]

def query(node, start, end, left, right):
    if end < left or right < start:
        return 0

    if lazy[node]:
        lazy[node * 2] += lazy[node]
        lazy[node * 2 + 1] += lazy[node]
        seg[node] += (end - start + 1) * lazy[node]

    if left <= start and end <= right:
        return seg[node]
    else:
        mid = (start + end) // 2
        ret = query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)
        seg[node] = seg[node * 2] + seg[node * 2 + 1]
        return ret

def update(node, start, end, left, right, w):
    if end < left or right < start:
        return

    if left <= start and end <= right:
        lazy[node] += w
    else:
        mid = (start + end) // 2
        update(node * 2, start, mid, left, right, w)
        update(node * 2 + 1, mid + 1, end, left, right, w)
    return

for i in range(1, n + 1):
    a = int(input())
    init_tree(1, 1, n, i, i, a)

for _ in range(m + k):
    q = list(map(int, input().split()))
    if q[0] == 1:
        update(1, 1, n, q[1], q[2], q[3])
    else:
        print(query(1, 1, n, q[1], q[2]))
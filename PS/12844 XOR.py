import sys
input = sys.stdin.readline

n = int(input())
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

def update(node, start, end, left, right, w):
    push(node, start, end)
    if end < left or right < start:
        return

    if left <= start and end <= right:
        lazy[node] ^= w
        push(node, start, end)
        return

    mid = (start + end) // 2
    update(node*2, start, mid, left, right, w)
    update(node*2+1, mid+1, end, left, right, w)
    seg[node] = seg[node*2] ^ seg[node*2+1]
    return

def push(node, start, end):
    if lazy[node]:
        seg[node] = (end - start + 1) - seg[node]
        if start < end:
            lazy[node*2] ^= lazy[node]
            lazy[node*2+1] ^= lazy[node]
        lazy[node] = 0
    return

def init_tree(arr, node, start, end):
    if start == end:
        seg[node] = arr[start - 1]
        return

    mid = (start + end) // 2
    init_tree(arr, node*2, start, mid)
    init_tree(arr, node*2+1, mid+1, end)
    seg[node] = seg[node*2] ^ seg[node*2+1]

arr = list(map(int, input().split()))
init_tree(arr, 1, 1, n)

for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        update(1, 1, n, q[1], q[2], q[3])
    else:
        print(query(1, 1, n, q[1], q[2]))
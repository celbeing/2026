import sys
input = sys.stdin.readline

n = int(input())
seg = [0] * n * 4
lazy = [0] * n * 4
arr = list(map(int, input().split()))

def init_tree(node, start, end):
    if start == end:
        seg[node] = arr[start-1]
        return

    mid = (start + end) // 2
    init_tree(node*2, start, mid)
    init_tree(node*2+1, mid+1, end)

    seg[node] = seg[node*2] ^ seg[node*2+1]
    return

def query(node, start, end, left, right):
    push(node, start, end)
    if end < left or right < start:
        return 0

    if left <= start and end <= right:
        return seg[node]

    mid = (start + end) // 2
    ret = query(node*2, start, mid, left, right) ^ query(node*2+1, mid+1, end, left, right)
    seg[node] = seg[node*2] ^ seg[node*2+1]
    return ret

def update(node, start, end, left, right, k):
    push(node, start, end)
    if end < left or right < start:
        return

    if left <= start and end <= right:
        if (end - start + 1) % 2:
            seg[node] ^= k
        if start < end:
            lazy[node*2] ^= k
            lazy[node*2+1] ^= k
        return

    mid = (start + end) // 2
    update(node*2, start, mid, left, right, k)
    update(node*2+1, mid+1, end, left, right, k)

    seg[node] = seg[node*2] ^ seg[node*2+1]
    return

def push(node, start, end):
    if lazy[node] != 0:
        leaf = end - start + 1
        if leaf % 2:
            seg[node] ^= lazy[node]

        if start < end:
            lazy[node*2] ^= lazy[node]
            lazy[node*2+1] ^= lazy[node]
        lazy[node] = 0
    return

init_tree(1, 1, n)
for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        update(1, 1, n, q[1]+1, q[2]+1, q[3])
    else:
        print(query(1, 1, n, q[1]+1, q[2]+1))
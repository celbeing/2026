import sys
input = sys.stdin.readline

n = int(input())
seg = [0] * n * 4
lazy = [0] * n * 4
arr = list(map(int, input().split()))

def init_tree(node, start, end):
    if start == end:
        seg[node] = arr[start - 1]
        return

    mid = (start + end) // 2
    init_tree(node*2, start, mid)
    init_tree(node*2+1, mid+1, end)

    seg[node] = seg[node*2] ^ seg[node*2+1]
    return

init_tree(1, 1, n)

def push()
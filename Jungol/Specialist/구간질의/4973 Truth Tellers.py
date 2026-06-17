import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    size = 1
    while size < n:
        size <<= 1
    sum_seg = [0] * size * 2
    cnt_seg = [0] * size * 2
    lazy = [0] * size * 2
    max_seg = [0] * size * 2

    def apply(node, value):
        sum_seg[node] += value * cnt_seg[node]
        lazy[node] += value

    def pull(node):
        if node < size:
            sum_seg[node] = sum_seg[node*2] + sum_seg[node*2+1]

    def push(node):
        if lazy[node]:
            if node < size:
                apply(node*2, lazy[node])
                apply(node*2+1, lazy[node])
            lazy[node] = 0

    def push_path(node):
        stack = []
        node >>= 1
        while node:
            stack.append(node)
            node >>= 1
        for x in reversed(stack):
            push(x)

    def build(node):
        node >>= 1
        while node:
            pull(node)
            sum_seg[node] += lazy[]
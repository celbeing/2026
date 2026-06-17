import sys
input = sys.stdin.readline

def solution():
    ray = int(input())

    y_set = set()
    plate = []
    for _ in range(int(input())):
        n, x, y1, y2 = map(int, input().split())
        y_set.add(y1); y_set.add(y2)
        plate.append((x, y1, y2, n))
    plate.sort()

    y_map = dict()
    for i, y in enumerate(sorted(list(y_set))):
        y_map[y] = i
    y_cnt = len(y_set)

    size = 1
    while size < y_cnt:
        size <<= 1

    seg = [0] * size * 2
    lazy = [0] * size * 2
    for i in range(1, y_cnt+size):
        seg[i] = ray

    def query(l, r):
        res = 0
        left, right = l+size, r+size

        push_path(l+size)
        push_path(r-1+size)

        while left < right:
            if left & 1:
                res = max(res, seg[left])
                left += 1
            if right & 1:
                right -= 1
                res = max(res, seg[right])
            left >>= 1; right >>= 1
        return res

    def apply(node, value):
        seg[node] -= value
        lazy[node] += value

    def pull(node):
        if node < size:
            seg[node] = max(seg[node*2], seg[node*2+1])

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
            seg[node] -= lazy[node]
            node >>= 1

    def update(l, r, value):
        left, right = l+size, r+size
        push_path(l+size)
        push_path(r-1+size)

        while left < right:
            if left & 1:
                apply(left, value)
                left += 1
            if right & 1:
                right -= 1
                apply(right, value)
            left >>= 1
            right >>= 1

        build(l+size)
        build(r-1+size)

    res = []
    for x, y1, y2, n in plate:
        y1, y2 = y_map[y1], y_map[y2]
        if query(y1, y2) <= 0:
            res.append(n)
        else:
            update(y1, y2, 1)

    res.sort()
    if res:
        print(*res)
    else:
        print(0)

solution()
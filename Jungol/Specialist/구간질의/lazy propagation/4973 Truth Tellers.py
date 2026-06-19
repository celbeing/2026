import sys
input = sys.stdin.readline

class SegTree:
    def __init__(self, n):
        self.size = 1
        self.n = n
        INF = -500001
        while self.size < n:
            self.size <<= 1

        self.tree = [INF] * self.size * 2
        self.lazy = [0] * self.size * 2

        for i in range(n):
            self.tree[i+self.size] = -i
        for i in range(self.size-1, 0, -1):
            self.pull(i)

    def pull(self, node):
        if node < self.size:
            self.tree[node] = max(self.tree[node*2], self.tree[node*2+1])

    def apply(self, node, value):
        self.tree[node] += value
        self.lazy[node] += value

    def push(self, node):
        if self.lazy[node]:
            if node < self.size:
                self.apply(node*2, self.lazy[node])
                self.apply(node*2+1, self.lazy[node])
            self.lazy[node] = 0

    def push_path(self, node):
        stack = []
        node >>= 1
        while node:
            stack.append(node)
            node >>= 1
        for x in reversed(stack):
            self.push(x)

    def build(self, node):
        node >>= 1
        while node:
            self.pull(node)
            self.tree[node] += self.lazy[node]
            node >>= 1

    def update(self, left, right, value):
        left += self.size
        right += self.size
        l, r = left, right

        self.push_path(l)
        self.push_path(r-1)

        while left < right:
            if left & 1:
                self.apply(left, value)
                left += 1
            if right & 1:
                right -= 1
                self.apply(right, value)
            left >>= 1
            right >>= 1

        self.build(l)
        self.build(r-1)

    def query(self):
        self.push_path(self.size)
        self.push_path(self.n+self.size-1)
        x = 1
        while x < self.size:
            self.push(x)
            x <<= 1
            if self.tree[x+1] >= 0:
                x += 1
        return x-self.size


def solution():
    n = int(input())
    seg = SegTree(n+1)

    declair = [(0,0)]
    for _ in range(n):
        l, r = map(int, input().split())
        seg.update(l, r+1, 1)
        declair.append((l, r))

    res = [seg.query()]
    q = int(input())
    for _ in range(q):
        p, l, r = map(int, input().split())
        l0, r0 = declair[p]
        seg.update(l0, r0+1, -1)
        seg.update(l, r+1, 1)
        res.append(seg.query())
        declair[p] = (l, r)
    print(*res)
solution()
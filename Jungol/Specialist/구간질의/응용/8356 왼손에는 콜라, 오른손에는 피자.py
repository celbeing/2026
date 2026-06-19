import sys
input = sys.stdin.readline

INF = -float('inf')

class SegTree():
    def __init__(self, n, cola, pizz):
        self.size = 1
        while self.size < n:
            self.size <<= 1

        self.seg_c = [0] * self.size * 2
        self.seg_p = [0] * self.size * 2
        self.seg_t = [INF] * self.size * 2

        for i in range(n):
            self.seg_c[i+self.size] = cola[i]
            self.seg_p[i+self.size] = pizz[i]

        for i in range(self.size-1, 0, -1):
            l, r = i*2, i*2+1
            self.seg_c[i] = max(self.seg_c[l], self.seg_c[r])
            self.seg_p[i] = max(self.seg_p[l], self.seg_p[r])
            self.seg_t[i] = max(self.seg_t[l], self.seg_t[r], self.seg_c[l]+self.seg_p[r])

    def cola(self, i, x):
        i += self.size-1
        self.seg_c[i] = x
        i >>= 1

        while i:
            l, r = i*2, i*2+1
            self.seg_c[i] = max(self.seg_c[l], self.seg_c[r])
            self.seg_t[i] = max(self.seg_t[l], self.seg_t[r], self.seg_c[l]+self.seg_p[r])
            i >>= 1

    def pizz(self, i, x):
        i += self.size-1
        self.seg_p[i] = x
        i >>= 1

        while i:
            l, r = i*2, i*2+1
            self.seg_p[i] = max(self.seg_p[l], self.seg_p[r])
            self.seg_t[i] = max(self.seg_t[l], self.seg_t[r], self.seg_c[l]+self.seg_p[r])
            i >>= 1

    def query(self, l, r):
        l += self.size-1
        r += self.size-1

        stack = []
        r_stack = []
        while l < r:
            if l & 1:
                stack.append(l)
                l += 1
            if not(r & 1):
                r_stack.append(r)
                r -= 1
            l >>= 1
            r >>= 1
        if l == r:
            stack.append(l)
        stack += reversed(r_stack)

        l, t = INF, INF
        for node in stack:
            t = max(t, l+self.seg_p[node], self.seg_t[node])
            l = max(l, self.seg_c[node])
        return t
def solution():
    n = int(input())
    cola = list(map(int, input().split()))
    pizz = list(map(int, input().split()))
    seg = SegTree(n, cola, pizz)
    for _ in range(int(input())):
        q, i, x = map(int, input().split())
        if q == 1:
            seg.cola(i, x)
        elif q == 2:
            seg.pizz(i, x)
        else:
            print(seg.query(i, x))

solution()
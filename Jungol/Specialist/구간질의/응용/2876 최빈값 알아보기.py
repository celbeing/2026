import sys
input = sys.stdin.readline

class SegTree():
    def __init__(self, arr):
        INF = -10**6
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1

        self.l_seg = [0] * self.size * 2
        self.r_seg = [0] * self.size * 2
        self.t_seg = [0] * self.size * 2

        self.l = [INF] * self.size * 2
        self.r = [INF] * self.size * 2
        self.t = [INF] * self.size * 2

        for i in range(self.n):
            self.l_seg[i+self.size] = 1
            self.r_seg[i+self.size] = 1
            self.t_seg[i+self.size] = 1

            self.l[i+self.size] = arr[i]
            self.r[i+self.size] = arr[i]

        for i in range(self.size-1, 0, -1):
            left = i*2
            right = i*2+1
            if self.l[right] == INF:
                self.l_seg[i] = self.l_seg[left]
                self.r_seg[i] = self.r_seg[left]
                self.t_seg[i] = self.t_seg[left]

                self.l[i] = self.l[left]
                self.r[i] = self.r[left]
            else:
                self.l[i] = self.l[left]
                if self.l[left] == self.l[right]:
                    self.l_seg[i] = self.t_seg[left]+self.l_seg[right]
                else:
                    self.l_seg[i] = self.l_seg[left]

                self.r[i] = self.r[right]
                if self.r[left] == self.r[right]:
                    self.r_seg[i] = self.r_seg[left] + self.t_seg[right]
                else:
                    self.r_seg[i] = self.r_seg[right]

                self.t_seg[i] = self.t_seg[left]
                if self.t_seg[i] < self.t_seg[right]:
                    self.t_seg[i] = self.t_seg[right]
                if self.t_seg[i] < self.l_seg[i]:
                    self.t_seg[i] = self.l_seg[i]
                if self.t_seg[i] < self.r_seg[i]:
                    self.t_seg[i] = self.r_seg[i]
                if self.r[left] == self.l[right] and self.t_seg[i] < self.r_seg[left] + self.l_seg[right]:
                    self.t_seg[i] = self.r_seg[left] + self.l_seg[right]

    def query(self, s, e):
        stack = []
        r_stack = []

        s, e = self.size+s, self.size+e
        while s < e:
            if s & 1:
                stack.append(s)
                s += 1
            if not(e & 1):
                r_stack.append(e)
                e -= 1
            s >>= 1
            e >>= 1
        if s == e:
            stack.append(s)
        stack += reversed(r_stack)

        res = 0

        left = 0
        l = self.l[stack[0]]
        for node in stack:
            if l != self.l[node]: break
            else: left += self.l_seg[node]

        right = 0
        r = self.r[stack[-1]]
        for node in reversed(stack):
            if r != self.r[node]: break
            else: right += self.r_seg[node]

        res = max(left, right)

        r, right, total = -10**6, 0, self.l_seg[stack[0]]
        for node in stack:
            total = max(total, self.t_seg[node])
            if r == self.l[node]:
                total = max(total, right + self.l_seg[node])
            if r == self.r[node]:
                right += self.r_seg[node]
                total = max(total, right)
            else:
                r = self.r[node]
                right = self.r_seg[node]
        res = max(res, total)
        return res

def solution():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    seg = SegTree(a)
    for _ in range(q):
        s, e = map(int, input().split())
        print(seg.query(s-1, e-1))

solution()
import sys
input = sys.stdin.readline

INF = -float('inf')

class SegTree():
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size <<= 1

        self.seg_l = [0] * self.size * 2
        self.seg_r = [0] * self.size * 2
        self.seg_t = [0] * self.size * 2
        self.l_end = [-1] * self.size * 2
        self.r_end = [-1] * self.size * 2
        self.cnt = [0] * self.size * 2

        for i in range(n):
            self.seg_l[i+self.size] = 1
            self.seg_r[i+self.size] = 1
            self.seg_t[i+self.size] = 1
            self.l_end[i+self.size] = 1
            self.r_end[i+self.size] = 1
            self.cnt[i+self.size] = 1
        for i in range(self.size-1,0,-1):
            self.seg_l[i] = 1
            self.seg_r[i] = 1
            self.seg_t[i] = 1
            if self.l_end[i*2] == -1:
                self.l_end[i] = -1
                self.r_end[i] = -1
            else:
                self.l_end[i] = 1
                self.r_end[i] = 1
            self.cnt[i] = self.cnt[i*2] + self.cnt[i*2+1]

    def update(self, i):
        i += self.size-1
        self.l_end[i] ^= 1
        self.r_end[i] ^= 1
        i >>= 1

        while i:
            left = i*2
            right = left+1
            if self.r_end[right] == -1:
                self.l_end[i] = self.l_end[left]
                self.r_end[i] = self.r_end[left]
                self.seg_l[i] = self.seg_l[left]
                self.seg_r[i] = self.seg_r[left]
                self.seg_t[i] = self.seg_t[left]
            else:
                self.l_end[i] = self.l_end[left]
                self.r_end[i] = self.r_end[right]

                if self.r_end[left] != self.l_end[right] and self.seg_l[left] == self.cnt[left]:
                    self.seg_l[i] = self.cnt[left] + self.seg_l[right]
                else:
                    self.seg_l[i] = self.seg_l[left]

                if self.r_end[left] != self.l_end[right] and self.seg_r[right] == self.cnt[right]:
                    self.seg_r[i] = self.seg_r[left] + self.cnt[right]
                else:
                    self.seg_r[i] = self.seg_r[right]

                self.seg_t[i] = max(self.seg_l[i], self.seg_r[i], self.seg_t[left], self.seg_t[right])
                if self.r_end[left] != self.l_end[right]:
                    self.seg_t[i] = max(self.seg_t[i], self.seg_r[left] + self.seg_l[right])

            i >>= 1

        return self.seg_t[1]

def solution():
    n, q = map(int, input().split())
    seg = SegTree(n)
    for _ in range(q):
        print(seg.update(int(input())))

solution()
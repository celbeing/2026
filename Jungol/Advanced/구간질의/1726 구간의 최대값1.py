import sys
input = sys.stdin.readline

n, q = map(int, input().split())
size = 1
while size < n:
    size <<= 1
seg = [0] * size * 2

for i in range(n):
    seg[size+i] = int(input())
for i in range(size-1,0,-1):
    seg[i] = max(seg[i*2], seg[i*2+1])

for _ in range(q):
    l, r = map(int, input().split())
    l, r = l+size-1, r+size-1
    res = 0
    while l < r:
        if l & 1:
            res = max(res, seg[l])
            l += 1
        l >>= 1
        if not(r & 1):
            res = max(res, seg[r])
            r -= 1
        r >>= 1
    if l == r:
        res = max(res, seg[l])
    print(res)
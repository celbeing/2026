import sys
input = sys.stdin.readline

n, q = map(int, input().split())
size = 1
while size < n:
    size <<= 1
max_seg = [0] * size * 2
min_seg = [1e9] * size * 2
for i in range(size,size+n):
    max_seg[i] = min_seg[i] = int(input())
for i in range(size-1,0,-1):
    max_seg[i] = max(max_seg[i*2],max_seg[i*2+1])
    min_seg[i] = min(min_seg[i*2],min_seg[i*2+1])

for _ in range(q):
    l, r = map(int, input().split())
    l, r = l+size-1, r+size-1
    max_res = 0
    min_res = 1e9

    while l < r:
        if l & 1:
            max_res = max(max_res, max_seg[l])
            min_res = min(min_res, min_seg[l])
            l += 1
        l >>= 1
        if not(r & 1):
            max_res = max(max_res, max_seg[r])
            min_res = min(min_res, min_seg[r])
            r -= 1
        r >>= 1
    if l == r:
        max_res = max(max_res, max_seg[l])
        min_res = min(min_res, min_seg[l])

    print(max_res - min_res)
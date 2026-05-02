import sys
input = sys.stdin.readline

n, m = map(int, input().split())
box = list(map(int, input().split()))
stf = list(map(int, input().split()))

size = 1
while size < n:
    size <<= 1
seg = [0] * size * 2
for i in range(n):
    seg[size+i] = box[i]
for i in range(size-1,0,-1):
    seg[i] = max(seg[i*2],seg[i*2+1])

res = [0] * m
for i in range(m):
    t = stf[i]
    if seg[1] < t: continue
    idx = 1
    while idx < size:
        if seg[idx*2] >= t:
            idx <<= 1
        else:
            idx <<= 1
            idx += 1
    res[i] = idx-size+1
    seg[idx] -= t
    idx >>= 1
    while idx:
        seg[idx] = max(seg[idx*2],seg[idx*2+1])
        idx >>= 1
print(*res)
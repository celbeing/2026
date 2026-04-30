import sys
input = sys.stdin.readline

n, m = map(int, input().split())
size = 1
while size < n:
    size <<= 1
seg = [0] * size * 2
for i, a in enumerate(list(map(int, input().split()))):
    seg[size+i] = a
for i in range(size-1,0,-1):
    seg[i] = seg[i*2]+seg[i*2+1]

for _ in range(m):
    l,i,r,s,j,e = map(int, input().split())
    l += size-1
    i += size-1
    r += size-1
    s += size-1
    j += size-1
    e += size-1

    upper, lower = 0, 0
    while l < r:
        if l & 1:
            upper += seg[l]
            l += 1
        l >>= 1
        if not(r & 1):
            upper += seg[r]
            r -= 1
        r >>= 1
    if l == r:
        upper += seg[l]

    while s < e:
        if s & 1:
            lower += seg[s]
            s += 1
        s >>= 1
        if not(e & 1):
            lower += seg[e]
            e -= 1
        e >>= 1
    if s == e:
        lower += seg[s]

    if upper > lower:
        res = (seg[j]+1)//2
        seg[i] += res
        seg[j] -= res
        i >>= 1
        j >>= 1
        while i:
            seg[i] += res
            seg[j] -= res
            i >>= 1
            j >>= 1
    elif upper < lower:
        res = (seg[i]+1)//2
        seg[i] -= res
        seg[j] += res
        i >>= 1
        j >>= 1
        while i:
            seg[i] -= res
            seg[j] += res
            i >>= 1
            j >>= 1

print(*seg[size:size+n])
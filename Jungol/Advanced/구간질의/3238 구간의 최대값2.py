import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = -float('inf')
size = 1
while size < n:
    size <<= 1
seg = [INF] * size * 2

for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        k, val = query[1:]
        k += size-1
        seg[k] = val
        k >>= 1
        while k:
            seg[k] = max(seg[k*2], seg[k*2+1])
            k >>= 1
    elif query[0] == 2:
        s, e = query[1:]
        s, e = s+size-1, e+size-1
        res = INF
        while s < e:
            if s & 1:
                res = max(res, seg[s])
                s += 1
            s >>= 1
            if not(e & 1):
                res = max(res, seg[e])
                e -= 1
            e >>= 1
        if s == e:
            res = max(res, seg[s])

        if res != INF:
            print(res)
    else:
        k = query[1]+size-1
        seg[k] = INF
        k >>= 1
        while k:
            seg[k] = max(seg[k*2], seg[k*2+1])
            k >>= 1
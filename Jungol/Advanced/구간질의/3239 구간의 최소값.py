import sys
input = sys.stdin.readline

n, m = map(int, input().split())
size = 1
while size < n:
    size <<= 1
INF = float('inf')
seg = [INF] * size * 2
idx = [INF] * size * 2
for i in range(n):
    idx[size+i] = i+1
for i in range(size-1,0,-1):
    idx[i] = min(idx[i*2], idx[i*2+1])

for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        k, val = query[1:]
        k += size-1
        seg[k] = val
        k >>= 1
        while k:
            if seg[k*2] <= seg[k*2+1]:
                seg[k] = seg[k*2]
                idx[k] = idx[k*2]
            else:
                seg[k] = seg[k*2+1]
                idx[k] = idx[k*2+1]
            k >>= 1
    else:
        s, e = query[1:]
        s, e = s+size-1, e+size-1
        res = INF
        index = 0
        res_back = INF
        index_back = 0
        while s < e:
            if s & 1:
                if seg[s] < res:
                    res = seg[s]
                    index = idx[s]
                s += 1
            s >>= 1
            if not(e & 1):
                if seg[e] <= res_back:
                    res_back = seg[e]
                    index_back = idx[e]
                e -= 1
            e >>= 1
        if s == e:
            if seg[s] < res:
                res = seg[s]
                index = idx[s]
        target = index_back
        if res <= res_back:
            target = index

        if query[0] == 2:
            if seg[target+size-1] != INF:
                print(target)
        else:
            target += size-1
            seg[target] = INF
            target >>= 1
            while target:
                if seg[target*2] <= seg[target*2+1]:
                    seg[target] = seg[target*2]
                    idx[target] = idx[target*2]
                else:
                    seg[target] = seg[target*2+1]
                    idx[target] = idx[target*2+1]
                target >>= 1
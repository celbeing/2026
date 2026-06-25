def solution():
    n = int(input())
    tire = []
    di = set()
    for _ in range(n):
        i, o, p = map(int, input().split())
        di.add(i)
        di.add(o)
        tire.append((i, o, p))
    di_map = dict()

    for i, x in enumerate(sorted(list(di))):
        di_map[x] = i
    for k in range(n):
        i, o, p = tire[k]
        i, o = di_map[i], di_map[o]
        tire[k] = (i, o, p)

    tire.sort(key=lambda x:x[1])

    size = 1
    while size < len(di):
        size <<= 1
    seg = [0] * size * 2

    def update(i, x):
        i += size
        seg[i] = x
        i >>= 1
        while i:
            seg[i] = max(seg[i*2], seg[i*2+1])
            i >>= 1

    def query(k):
        l, r = size, size+k+1
        res = 0
        while l < r:
            if l & 1:
                res = max(res, seg[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, seg[r])
            l >>= 1
            r >>= 1
        return res

    for i, o, p in tire:
        t = query(i)+p
        if seg[size+o] < t:
            update(o, t)
    print(seg[1])
solution()
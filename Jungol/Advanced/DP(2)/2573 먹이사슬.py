def solution():
    n = int(input())
    cord = set()
    check = set()
    for _ in range(n):
        i, l, r = map(int, input().split())
        cord.add(l); cord.add(r)
        if (l, r) in check: continue
        check.add((l, r))
    cord_map = dict()
    for i, c in enumerate(sorted(list(cord))):
        cord_map[c] = i
    animal = sorted(list(check), key=lambda x:(x[1], -x[0]))
    n = len(animal)
    for i in range(n):
        animal[i] = (cord_map[animal[i][0]], cord_map[animal[i][1]])

    k = len(cord)
    size = 1
    while size < k:
        size <<= 1
    seg = [0] * (size * 2)

    def update(i, x):
        k = i+size
        seg[k] = x
        k >>= 1
        while k:
            seg[k] = max(seg[k*2], seg[k*2+1])
            k >>= 1

    def query(l, r):
        l, r = l+size, r+size
        res = 0
        while l < r:
            if l & 1:
                res = max(res, seg[l])
                l += 1
            if not(r & 1):
                res = max(res, seg[r])
                r -= 1
            l >>= 1
            r >>= 1
        if l == r:
            res = max(res, seg[l])
        return res

    for l, r in animal:
        k = query(l, r)
        update(l, k+1)

    print(query(0, len(cord)-1))

solution()
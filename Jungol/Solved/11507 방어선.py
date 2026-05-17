import sys
input = sys.stdin.readline

z = int(input())
for _ in range(z):
    n = int(input())
    a = list(map(int, input().split()))
    l = [1] * n
    r = [1] * n
    for i in range(1, n):
        if a[i] > a[i-1]:
            l[i] = l[i-1]+1
    for i in range(n-2,-1,-1):
        if a[i] < a[i+1]:
            r[i] = r[i+1]+1

    # 탑 높이 좌표압축
    a_set = set()
    a_set.update(a)
    a_map = dict()
    for i, k in enumerate(sorted(list(a_set))):
        a_map[k] = i

    length = len(a_set)
    size = 1
    while size < length:
        size <<= 1
    seg = [0] * size * 2

    def query(h):
        l, r = size, size+a_map[h]
        res = 0
        while l < r:
            if l & 1:
                res = max(res, seg[l])
                l += 1
            l >>= 1
            if r & 1:
                r -= 1
                res = max(res, seg[r])
            r >>= 1
        return res

    def update(h, val):
        x = size+a_map[h]
        if seg[x] < val:
            seg[x] = val
            x >>= 1
            while x:
                seg[x] = max(seg[x*2], seg[x*2+1])
                x >>= 1

    ans = 0
    for i in range(n):
        ans = max(ans, query(a[i])+r[i])
        update(a[i],l[i])
    print(ans)
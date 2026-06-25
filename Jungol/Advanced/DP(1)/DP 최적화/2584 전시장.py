def solution():
    n, s = map(int, input().split())
    pic = [tuple(map(int, input().split())) for _ in range(n)]
    pic.sort()
    dp = [0] * (n+1)

    size = 1
    while size < n:
        size <<= 1
    seg = [0] * size * 2

    def update(i, x):
        i += size
        seg[i] = x
        i >>= 1
        while i:
            seg[i] = max(seg[i*2], seg[i*2+1])
            i >>= 1

    def query(i):
        l, r = size, size+i
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
    x = 0
    while pic[x][0] < s:
        dp[x] = pic[x][1]
        update(x, dp[x])
        x += 1
    idx = 0
    for i in range(x, n):
        h, c = pic[i]
        while h-s >= pic[idx][0]:
            idx += 1
        dp[i] = query(idx)+c
        update(i, dp[i])
    print(max(dp))
solution()
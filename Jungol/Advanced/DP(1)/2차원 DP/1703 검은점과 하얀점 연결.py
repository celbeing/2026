def solution():
    n = int(input())
    a = list(map(int, list(input().strip())))

    res = 0
    INF = float('inf')
    memo = [[0] * n for _ in range(n)]
    high = [[0] * n for _ in range(n)]
    path = [[-1] * n for _ in range(n)]


    for i in range(n-1):
        if a[i] != a[i+1]:
            memo[i][i+1] = 3
            high[i][i+1] = 1
            path[i][i+1] = 0

    def dp(i, j):
        if i >= j: return INF, INF
        elif high[i][j]: return memo[i][j], high[i][j]

        ret, h = INF, INF
        if a[i] != a[j]:
            ret, h = dp(i+1, j-1)
            h += 1
            ret += h*2 + j - i
            path[i][j] = 0

        for k in range(i+1, j):
            ret_l, h_l = dp(i, k)
            ret_r, h_r = dp(k+1, j)
            ret_t, h_t = ret_l+ret_r, max(h_l, h_r)
            if ret > ret_t:
                ret = ret_t
                h = h_t
                path[i][j] = k

        memo[i][j] = ret
        high[i][j] = h

        return ret, h

    result, h = dp(0, n-1)
    print(result)
    link = []
    def link_find(i, j):
        if i >= j: return
        if path[i][j] == 0:
            link.append((i+1, j+1))
            link_find(i+1, j-1)
        else:
            link_find(i, path[i][j])
            link_find(path[i][j]+1, j)

    link_find(0, n-1)
    link.sort()
    for x, y in link:
        print(x, y)

solution()
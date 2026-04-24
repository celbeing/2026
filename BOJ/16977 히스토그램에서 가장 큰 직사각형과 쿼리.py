import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def solution():
    n = int(input())
    h = list(map(int, input().split()))

    sorted_h = sorted([(h, i+1) for i, h in enumerate(h)], reverse=True)

    size = n*40
    tree_max = [0]*size
    tree_l = [0]*size
    tree_r = [0]*size
    tree_all = [0]*size
    left = [0]*size
    right = [0]*size
    node_cnt = 0

    def update(pre, s, e, idx):
        nonlocal node_cnt
        node_cnt += 1
        now = node_cnt

        if s == e:
            tree_max[now] = tree_l[now] = tree_r[now] = 1
            tree_all[now] = 1
            return now

        m = (s+e)//2
        left[now], right[now] = left[pre], right[pre]

        if idx <= m:
            left[now] = update(left[pre], s, m, idx)
        else:
            right[now] = update(right[pre], m+1, e, idx)

        l, r = left[now], right[now]
        tree_all[now] = tree_all[l] & tree_all[r]
        tree_l[now] = tree_l[l] + (tree_l[r] if tree_all[l] else 0)
        tree_r[now] = tree_r[r] + (tree_r[l] if tree_all[r] else 0)
        tree_max[now] = max(tree_max[l], tree_max[r], tree_l[r]+tree_r[l])

        return now

    roots = [0]*(n+1)
    for i in range(n):
        roots[i+1] = update(roots[i], 1, n, sorted_h[i][1])

    def query(node, s, e, l, r):
        if l <= s and e <= r:
            return tree_max[node], tree_l[node], tree_r[node], tree_all[node]

        m = (s+e)//2
        if r <= m:
            return query(left[node], s, m, l, r)
        if l > m:
            return query(right[node], m+1, e, l, r)

        l_max, l_lc, l_rc, l_all = query(left[node], s, m, l, r)
        r_max, r_lc, r_rc, r_all = query(right[node], m+1, e, l, r)

        res_all = l_all & r_all
        res_l = l_lc + (r_lc if l_all else 0)
        res_r = r_rc + (l_rc if r_all else 0)
        res_max = max(l_max, r_max, l_rc+r_lc)

        return res_max, res_l, res_r, res_all

    for _ in range(int(input())):
        l, r, w = map(int, input().split())
        low, high, ans = 0, n-1, 0

        while low <= high:
            mid = (low+high)//2
            if query(roots[mid+1], 1, n, l, r)[0] >= w:
                ans = sorted_h[mid][0]
                high = mid - 1
            else:
                low = mid + 1
        print(ans)

solution()
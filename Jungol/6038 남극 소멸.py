import sys
input = sys.stdin.readline

def solution():
    n, q = map(int, input().split())
    size = 1
    while size < n:
        size <<= 1
    seg = [1] * size * 2

    h = list(map(int, input().split()))
    h_sorted = []
    for i, hh in enumerate(h):
        h_sorted.append((hh, i))
    h_sorted.sort()
    query = []
    for i in range(q):
        l, r, x = map(int, input().split())
        query.append((x, l, r, i))
    query.sort()

    idx = 0
    result = []
    for x, l, r, i in query:
        while idx < n and h_sorted[idx][0] <= x:
            t = h_sorted[idx][1]
            h[t] = 0
            t += size
            seg[t] = 0
            while t:
                # 대충 올라가면서 연속하지 않은 섬만 더하면서 갱신
        # l-1, r-1 구간에서 노드 탐색 끝내고, 연속하는 섬인 경우는 더하면서 1빼주기
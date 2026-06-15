import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def solution():
    INF = float('inf')
    n, m = map(int, input().split()); m -= 1
    link = [list(map(int, input().split())) for _ in range(n)]
    dist = [INF] * n
    income = [i for i in range(n)]
    dist[0] = 0
    hq = [(0,0)]

    while hq:
        d, now = heappop(hq)
        if dist[now] < d: continue
        for next in range(n):
            if now == next: continue

            nd = d + link[now][next]
            if dist[next] > nd:
                dist[next] = nd
                heappush(hq, (nd, next))
                income[next] = now

    res = [m+1]
    print(dist[m])
    while m:
        m = income[m]
        res.append(m+1)
    res.reverse()
    print(*res)

solution()
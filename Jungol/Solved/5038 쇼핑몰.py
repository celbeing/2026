import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def solution():
    INF = float('inf')
    n, m, k = map(int, input().split())
    graph = [dict() for _ in range(n+1)]
    edge = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w
        edge.append((u, v, w))

    dist = [INF] * (n+1)
    dijk = []
    for _ in range(k):
        x = int(input())
        dist[x] = 0
        heappush(dijk, (0, x))

    while dijk:
        d, now = heappop(dijk)
        if dist[now] < d: continue

        for next in graph[now]:
            nd = d + graph[now][next]
            if nd < dist[next]:
                dist[next] = nd
                heappush(dijk, (nd, next))

    res = 0
    for a, b, d in edge:
        res = max(res, (dist[a]+dist[b]+d+1)//2)

    print(res)

solution()
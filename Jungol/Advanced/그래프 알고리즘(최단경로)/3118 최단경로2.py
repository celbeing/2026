import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def solution():
    INF = float('inf')
    n, m = map(int, input().split())
    graph = [dict() for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int, input().split())
        if v in graph[u]:
            graph[u][v] = min(graph[u][v], w)
        else:
            graph[u][v] = w

    dist = [INF] * (n+1)
    hq = [(0, 1)]
    while hq:
        d, now = heappop(hq)
        if now == n: break
        if dist[now] < d: continue
        for next in graph[now]:
            nd = d + graph[now][next]
            if dist[next] > nd:
                dist[next] = nd
                heappush(hq, (nd, next))
    print(dist[n])
solution()
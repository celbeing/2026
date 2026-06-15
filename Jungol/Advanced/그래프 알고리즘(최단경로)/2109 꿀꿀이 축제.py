import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def solution():
    INF = float('inf')
    n, m, x = map(int,input().split())
    graph = [dict() for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int, input().split())
        if v in graph[u]:
            graph[u][v] = min(graph[u][v], w)
        else:
            graph[u][v] = w

    party = [INF]*(n+1)

    def dijkstra(s, e):
        hq = [(0, s)]
        dist = [INF]*(n+1)
        dist[s] = 0

        while hq:
            d, now = heappop(hq)
            if now == e: break

            if dist[now] < d: continue

            for next in graph[now]:
                nd = d + graph[now][next]
                if dist[next] > nd:
                    dist[next] = nd
                    heappush(hq, (nd, next))

        if e: return dist[e]
        else: return dist

    for i in range(1, n+1):
        party[i] = dijkstra(i, x)

    home = dijkstra(x, 0)

    res = 0
    for i in range(1, n+1):
        res = max(res, home[i]+party[i])
    print(res)
solution()
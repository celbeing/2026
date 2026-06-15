import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def solution():
    INF = float('inf')
    n, p, c = map(int, input().split())
    graph = [dict() for _ in range(p+1)]
    for _ in range(c):
        i, j, cost = map(int, input().split())
        if j in graph[i]:
            graph[i][j] = min(graph[i][j], cost)
        else:
            graph[i][j] = cost
        graph[j][i] = graph[i][j]

    pos = list(map(int, input().split()))
    place = [0] * (p+1)
    for k in pos:
        place[k] += 1
    result = [0] * (p+1)
    result[0] = INF

    def dijk(s):
        dist = [INF] * (p+1)
        dist[s] = 0
        hq = [(0, s)]
        while hq:
            d, now = heappop(hq)
            if dist[now] < d: continue

            for next in graph[now]:
                nd = graph[now][next] + d
                if dist[next] > nd:
                    dist[next] = nd
                    heappush(hq, (nd, next))

        k = place[s]
        for i in range(1, p+1):
            result[i] += dist[i] * k

    for i in range(1, p+1):
        if place[i]:
            dijk(i)
    print(min(result))
solution()
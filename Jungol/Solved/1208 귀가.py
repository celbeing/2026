import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = float('inf')

p = int(input())
alpha = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
node = dict()
for i, a in enumerate(alpha):
    node[a] = i

graph = [dict() for _ in range(52)]
dist = [INF] * 52
for _ in range(p):
    u, v, w = input().split()
    u, v, w = node[u], node[v], int(w)
    if v in graph[u]:
        if graph[u][v] > w:
            graph[u][v] = w
            graph[v][u] = w
    else:
        graph[u][v] = w
        graph[v][u] = w

dist[-1] = 0
hq = []
heappush(hq, (0, 51))
while hq:
    d, now = heappop(hq)
    if 25 < now < 51:
        print(alpha[now],d)
        break
    for next in graph[now]:
        if d + graph[now][next] < dist[next]:
            dist[next] = d + graph[now][next]
            heappush(hq, (dist[next], next))
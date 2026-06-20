from heapq import heappush, heappop
n, m, y = map(int, input().split())
graph = [dict() for _ in range(n+1)]
for _ in range(m):
    u, v, t = map(int, input().split())
    u -= 1
    v -= 1
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], t)
    else:
        graph[u][v] = t
    graph[v][u] = graph[u][v]
x = list(map(int, input().split()))
for i in range(n):
    graph[i][n] = x[i]+y
    graph[n][i] = x[i]

INF = float('inf')
dist = [INF] * (n+1)
dist[0] = 0
hq = [(0,0)]

while hq:
    d, now = heappop(hq)
    if dist[now] < d: continue
    for next in graph[now]:
        if d+graph[now][next] < dist[next]:
            dist[next] = d+graph[now][next]
            heappush(hq, (dist[next], next))

print(*dist[1:-1])
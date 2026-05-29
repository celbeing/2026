import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [{} for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w

dist = [int(1e9)] * (n+1)
def dijk():
    hq = [(0,1)]
    dist[1] = 0
    while hq:
        d, now = heappop(hq)
        if d > dist[now]: continue
        for next in graph[now]:
            nd = d + graph[now][next]
            if dist[next] > nd:
                heappush(hq, (nd, next))
                dist[next] = nd

dijk()

fast = dist[n]

route = [n]
now = n
while now > 1:
    for bef in graph[now]:
        if dist[bef] == dist[now] - graph[now][bef]:
            now = bef
            route.append(now)
            break
route.reverse()


res = 0
for i in range(len(route)-1):
    tmp = graph[route[i]][route[i+1]]
    graph[route[i]][route[i+1]] = int(1e9)
    graph[route[i+1]][route[i]] = int(1e9)
    dist = [int(1e9)] * (n+1)
    dijk()
    if dist[n] == int(1e9):
        res = -1
        break
    res = max(res, dist[n]-fast)
    graph[route[i]][route[i+1]] = tmp
    graph[route[i+1]][route[i]] = tmp
print(res)
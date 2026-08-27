import io
from collections import deque
input = io.BufferedReader(io.FileIO(0), 1 << 18).readline
INF = float('inf')

def solution(N, A, B):
    def connect(u, v, c=INF, d=0):
        graph[u].append(v)
        capa[u][v] = c
        flow[u][v] = 0
        cost[u][v] = d
        graph[v].append(u)
        capa[v][u] = 0
        flow[v][u] = 0
        cost[v][u] = -d

    graph = [[] for _ in range(N+4)]
    capa = [{} for _ in range(N+4)]
    flow = [{} for _ in range(N+4)]
    cost = [{} for _ in range(N+4)]

    connect(0, N+1, A)
    connect(0, N+2, B)
    for i in range(1, N+1):
        k, a, b = map(int, input().split())
        connect(N+1, i, INF, a)
        connect(N+2, i, INF, b)
        connect(i, N+3, k, 0)

    s, e = 0, N+3
    while True:
        visit = [-1] * (N+4)
        is_inQ = [0] * (N+4)
        dist = [INF] * (N+4)

        SPFA = deque([0])
        dist[s] = 0
        is_inQ[s] = 1

        while SPFA:
            now = SPFA.popleft()
            is_inQ[now] = 0
            for next in capa[now]:
                if capa[now][next] - flow[now][next] > 0 and dist[now] + cost[now][next] < dist[next]:
                    dist[next] = dist[now] + cost[now][next]
                    visit[next] = now
                    if is_inQ[next] == 0:
                        is_inQ[next] = 1
                        SPFA.append(next)
        if visit[e] == -1: break

        f = INF
        r = e
        while r != s:
            f = min(f, capa[visit[r]][r] - flow[visit[r]][r])
            r = visit[r]

        r = e
        while r != s:
            flow[visit[r]][r] += f
            flow[r][visit[r]] -= f
            r = visit[r]

    res = 0
    for i in range(1, N+1):
        res += flow[N+1][i] * cost[N+1][i]
        res += flow[N+2][i] * cost[N+2][i]
    return res

res = []
while True:
    N, A, B = map(int, input().split())
    if N == A == B == 0: break
    res.append(solution(N, A, B))
print(*res)
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

# u -> v 간선을 생성
# f: 최대 용량 / c: 비용
def link(u, v, f = 1, c = 0):
    capa[u][v] = f
    capa[v][u] = 0
    flow[u][v] = 0
    flow[v][u] = 0
    cost[u][v] = c
    cost[v][u] = -c

v, e = map(int, input().split())
node = v * 2 + 1
capa = [dict() for _ in range(node)]    # 간선 용량
flow = [dict() for _ in range(node)]    # 간선 유량
cost = [dict() for _ in range(node)]    # 간선 비용
for i in range(1, v + 1):
    link(i, i + v)
capa[1][v + 1] = 2
for _ in range(e):
    a, b, c = map(int ,input().split())
    link(a + v, b, 1, c)

res = 0
while 1:
    visit = [-1] * node
    is_inQ = [0] * node
    dist = [INF] * node

    spfa = deque([1])
    is_inQ[1] = 1
    dist[1] = 0

    # 남은 용량이 있는 최소 비용 경로 탐색
    while spfa:
        now = spfa.popleft()
        is_inQ[now] = 0

        for next in capa[now]:
            if capa[now][next] - flow[now][next] > 0 and dist[now] + cost[now][next] < dist[next]:
                dist[next] = dist[now] + cost[now][next]
                visit[next] = now
                if is_inQ[next] == 0:
                    is_inQ[next] = 1
                    spfa.append(next)

    # 더 이상 경로가 없는 경우
    if visit[v] == -1: break

    # 경로 역추적 하며 생성할 수 있는 최대 유량 탐색
    f = INF
    r = v
    while r != 1:
        f = min(f, capa[visit[r]][r] - flow[visit[r]][r])
        r = visit[r]

    # 경로 역추적하며 유량 생성
    r = v
    while r != 1:
        res += f * cost[visit[r]][r]
        flow[visit[r]][r] += f
        flow[r][visit[r]] -= f
        r = visit[r]
print(res)
from collections import deque

n = int(input())
m = int(input())

graph = [dict() for _ in range(n+1)]
need = [0] * (n+1)
count = [0] * (n+1)
for _ in range(m):
    x, y, k = map(int, input().split())
    graph[x][y] = k
    count[y] += 1
need[n] = 1
tp = deque()
for i in range(1, n+1):
    if count[i] == 0:
        tp.append(i)
order = []

while tp:
    now = tp.popleft()
    order.append(now)
    for next in graph[now]:
        count[next] -= 1
        if count[next] == 0:
            tp.append(next)

for now in order:
    for next in graph[now]:
        need[next] += graph[now][next] * need[now]

for i in range(1, n):
    if len(graph[i]) == 0:
        print(i, need[i])
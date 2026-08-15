from collections import deque

n = int(input())
link = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

bfs = deque([1])
now = 1
check = [0] * (n+1)

while bfs:
    now = bfs.popleft()
    for next in link[now]:
        if check[next] == 0:
            check[next] = 1
            bfs.append(next)

check = [0] * (n+1)
bfs = deque([now])

while bfs:
    now = bfs.popleft()
    for next in link[now]:
        if check[next] == 0:
            check[next] = check[now] + 1
            bfs.append(next)

print(check[now])
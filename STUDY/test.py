from collections import deque

n = int(input())
i,j = map(int, input().split())
d = [(1,0),(0,1),(-1,0),(0,-1)]
i -= 1; j -= 1
mount = [list(map(int, input().split())) for _ in range(n)]
INF = float('inf')
cost = [[INF] * n for _ in range(n)]
bfs = deque([(i,j)])
cost[i][j] = 0

res = INF
while bfs:
    x, y = bfs.popleft()
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if mount[x][y] < mount[nx][ny]:
                nc = cost[x][y] + mount[nx][ny] - mount[x][y]
            else:
                nc = cost[x][y] + (mount[x][y] - mount[nx][ny]) ** 2
            if nc < cost[nx][ny]:
                cost[nx][ny] = nc
                bfs.append((nx, ny))

        else:
            res = min(res, cost[x][y] + mount[x][y] ** 2)
print(res)
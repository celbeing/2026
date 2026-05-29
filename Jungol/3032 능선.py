import sys
from collections import deque
input = sys.stdin.readline

d = [(1,0),(0,1),(-1,0),(0,-1)]
h, w = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]
graph = [[[] for _ in range(w)] for _ in range(h)]
income = [[0] * w for _ in range(h)]
site = [[0] * w for _ in range(h)]
sink = []
for i in range(h):
    for j in range(w):
        for dx, dy in d:
            ni, nj = i+dx, j+dy
            if 0<=ni<h and 0<=nj<w:
                if grid[i][j] < grid[ni][nj]:
                    graph[i][j].append((ni,nj))
                    income[i][j] += 1
            else: income[i][j] += 1

for i in range(h):
    for j in range(w):
        if income[i][j] == 4:
            sink.append((i, j))


for i, j in sink:
    bfs = deque()
    bfs.append((i,j))
    check = set()
    while bfs:
        x, y = bfs.popleft()
        for nx, ny in graph[x][y]:
            if (nx, ny) in check: continue
            else:
                site[nx][ny] += 1
                check.add((nx, ny))
                bfs.append((nx, ny))

res = 0
for i in range(h):
    for j in range(w):
        if site[i][j] > 1:
            res += 1
print(res)
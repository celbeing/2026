import sys
from collections import deque
input = sys.stdin.readline
d = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]

h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]
n_grid = [['.']*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            continue
        for di,dj in d:
            ni,nj = i+di,j+dj
            if 0 <= ni < h and 0 <= nj < w:
                if grid[ni][nj] == '#':
                    n_grid[i][j] = '#'
                    break
for i in range(h):
    for j in range(w):
        grid[i][j] = n_grid[i][j]

cell = [[-1] * w for _ in range(h)]
bfs = deque()
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            cell[i][j] = 1
            bfs.append((i,j))
while bfs:
    x, y = bfs.popleft()
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and cell[nx][ny] == -1:
            cell[nx][ny] = cell[x][y] ^ 1
            bfs.append((nx,ny))

for i in range(h):
    for j in range(w):
        if cell[i][j] == 0:
            grid[i][j] = '#'
        else:
            grid[i][j] = '.'

for l in grid:
    print(''.join(l))
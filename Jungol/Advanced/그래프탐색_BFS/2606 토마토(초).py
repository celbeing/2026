import sys
from collections import deque
input = sys.stdin.readline

d = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
m,n,h = map(int, input().split())
tmt = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

count = 0
bfs = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tmt[i][j][k] == 1:
                bfs.append((i,j,k))
            elif tmt[i][j][k] == 0:
                count += 1
last = 1
while bfs:
    x, y, z = bfs.popleft()
    for dx, dy, dz in d:
        nx, ny, nz = x+dx, y+dy, z+dz
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
            if tmt[nx][ny][nz] == 0:
                tmt[nx][ny][nz] = tmt[x][y][z] + 1
                bfs.append((nx,ny,nz))
                if last < tmt[nx][ny][nz]:
                    last = tmt[nx][ny][nz]
                count -= 1

if count == 0: print(last-1)
else: print(-1)
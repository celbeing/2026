import sys
from collections import deque
input = sys.stdin.readline

def solution():
    INF = int(1e9)
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    h, w = map(int, input().split())
    grid = [input().strip() for _ in range(h)]
    dist = [[INF] * w for _ in range(h)]
    bfs = deque()
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'S':
                dist[i][j] = 0
                bfs.append(i*w+j)
            elif grid[i][j] == '#':
                dist[i][j] = -1

    while bfs:
        n = bfs.popleft()
        x, y = n//w, n%w
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < h and 0 <= ny < w and dist[nx][ny] == INF:
                dist[nx][ny] = dist[x][y] + 1
                if grid[nx][ny] == 'G':
                    bfs.clear()
                    print(dist[nx][ny])
                    break
                bfs.append(nx*w+ny)

solution()
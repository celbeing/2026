import sys
from collections import deque
input = sys.stdin.readline

def solution():
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]
    crash = [[10001] * m for _ in range(n)]
    x, y = 0, 0
    for i in range(m):
        if grid[x][i] == '#':
            x, y = 0, i-1
            break
    else:
        print(0)
        return
    crash[x][y] = 1
    bfs = deque([(x,y)])
    while bfs:
        x, y = bfs.popleft()
        for dx, dy in d:
            nx, ny = x, y
            while True:
                if nx+dx < 0 or nx+dx == n or ny+dy < 0: break
                if ny+dy == m:
                    print(crash[x][y])
                    return
                if grid[nx+dx][ny+dy] == '#':
                    if crash[x][y] >= crash[nx][ny]: break
                    bfs.append((nx, ny))
                    crash[nx][ny] = crash[x][y] + 1
                    break
                nx += dx
                ny += dy
    print(-1)

solution()
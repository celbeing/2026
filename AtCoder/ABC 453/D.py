import sys
input = sys.stdin.readline
from collections import deque

def solution():
    h, w = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]
    check = [[0] * w for _ in range(h)]
    d = [(1,0,'D',1),(0,1,'R',2),(-1,0,'U',4),(0,-1,'L',8)]

    bfs = deque()
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'S':
                bfs.append((i,j,''))
                check[i][j] = 15
                break
        if bfs:
            break

    flag = False
    while bfs:
        x, y, r = bfs.popleft()
        for dx, dy, dr, bit in d:
            if grid[x][y] == 'x' and r[-1] == dr: continue

            nx, ny, nr = x + dx, y + dy, r + dr
            while 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 'o':
                check[nx][ny] |= bit
                nx += dx
                ny += dy
                nr += dr

            if 0 <= nx < h and 0 <= ny < w:
                if grid[nx][ny] == '#' or check[nx][ny] & bit: continue
                elif grid[nx][ny] == 'G':
                    flag = True
                    print('Yes')
                    print(nr)
                    break

                if grid[nx][ny] == '.': bit = 15
                check[nx][ny] |= bit
                bfs.append((nx,ny,nr))
        if flag: break
    else:
        print('No')
solution()
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def solution():
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    n = int(input())
    grid = [list(map(int, list(input().strip()))) for _ in range(n)]

    check = [[2500] * n for _ in range(n)]
    check[0][0] = 0
    hq = [(0,0,0)]

    while hq:
        c, x, y = heappop(hq)
        if x == n-1 and y == n-1: break
        if check[x][y] < c: continue
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n:
                if grid[nx][ny] == 0 and check[nx][ny] > c+1:
                    check[nx][ny] = c + 1
                    heappush(hq, (c+1, nx, ny))
                elif grid[nx][ny] == 1 and check[nx][ny] > c:
                    check[nx][ny] = c
                    heappush(hq, (c, nx, ny))
    print(check[-1][-1])

solution()
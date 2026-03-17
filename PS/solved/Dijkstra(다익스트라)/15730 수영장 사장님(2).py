import sys
from heapq import heappush, heappop
input = sys.stdin.readline

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n,m = map(int, input().split())
pool = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]
wall = []
result = 0

for i in range(m):
    heappush(wall, (pool[0][i], 0, i))
    check[0][i] = 1
for i in range(1, n):
    heappush(wall, (pool[i][0], i, 0))
    check[i][0] = 1
if n > 1:
    for i in range(1, m):
        heappush(wall, (pool[-1][i], n - 1, i))
        check[-1][i] = 1
if m > 1:
    for i in range(1, n - 1):
        heappush(wall, (pool[i][-1], i, m - 1))
        check[i][-1] = 1

while wall:
    h, x, y = heappop(wall)
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and check[nx][ny] == 0:
            check[nx][ny] = 1
            if pool[nx][ny] < h:
                result += h - pool[nx][ny]
                pool[nx][ny] = h
            heappush(wall, (pool[nx][ny], nx, ny))

print(result)
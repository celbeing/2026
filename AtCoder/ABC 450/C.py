import sys
input = sys.stdin.readline
from collections import deque
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]
check = [[0] * w for _ in range(h)]
count = 0

for i in range(h):
    for j in range(w):
        if grid[i][j] == '.' and check[i][j] == 0:
            bfs = deque([(i, j)])
            check[i][j] = 1
            flag = True
            while bfs:
                x, y = bfs.popleft()
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w:
                        if grid[nx][ny] == '.' and check[nx][ny] == 0:
                            check[nx][ny] = 1
                            bfs.append((nx, ny))
                    else:
                        flag = False

            if flag:
                count += 1

print(count)
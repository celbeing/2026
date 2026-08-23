from collections import deque

d = [(1,0), (0,1), (-1,0), (0,-1)]
h,w,k = map(int, input().split())
grid = [input().strip() for _ in range(h)]
bfs = deque()

safe_row = []
safe_col = []
count = 0
check = [[-1] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            break
    else:
        safe_row.append(i)
for j in range(w):
    for i in range(h):
        if grid[i][j] == '#':
            break
    else:
        safe_col.append(j)

for r in safe_row:
    for c in safe_col:
        bfs.append((r, c))
        check[r][c] = 0
        count += 1

while bfs:
    x, y = bfs.popleft()
    dist = check[x][y]
    if dist == k: continue
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0 <= nx < h and 0 <= ny < w and check[nx][ny] == -1 and grid[nx][ny] == '.':
            check[nx][ny] = dist+1
            count += 1
            bfs.append((nx, ny))
print(count)
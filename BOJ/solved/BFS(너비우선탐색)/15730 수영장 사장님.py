import sys
from heapq import heappush, heappop
from collections import deque
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    pool = [[0 for _ in range(m + 2)]] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0 for _ in range(m + 2)]]
    fill = [[0] * (m + 2) for _ in range(n + 2)]
    hq = []
    res = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            heappush(hq, (-pool[i][j], i, j))

    while hq:
        h, i, j = heappop(hq)
        if fill[i][j] > 0: continue

        border = 10001
        bfs = deque([(i, j)])
        area = set()
        area.add((i, j))
        while bfs:
            x, y = bfs.popleft()
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 < nx <= n and 0 < ny <= m:
                    if pool[nx][ny] > pool[i][j]:
                        border = min(border, pool[nx][ny])
                    elif fill[nx][ny] == 0 and not((nx, ny) in area):
                        bfs.append((nx, ny))
                        area.add((nx, ny))
                else:
                    bfs.clear()
                    area.clear()
                    break

        if border < 10001:
            for x, y in area:
                fill[x][y] = border
                res += max(fill[x][y] - pool[x][y], 0)
    print(res)
solution()
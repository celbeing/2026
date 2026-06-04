import sys
input = sys.stdin.readline

def solution():
    d = [(1,0), (0,1), (-1,0), (0,-1)]

    h, w = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(h)]
    low = []
    for i in range(h):
        for j in range(w):
            low.append((grid[i][j], i, j))
    low.sort()

    sink = [[0] * w for _ in range(h)]

    count = 1
    result = 0
    for _, i, j in low:
        for dx, dy in d:
            nx, ny = i+dx, j+dy
            if 0<=nx<h and 0<=ny<w and grid[nx][ny] < grid[i][j]:
                sink[i][j] |= sink[nx][ny]
            if sink[i][j].bit_count() >= 2: break

        if sink[i][j] == 0:
            sink[i][j] = count
            count <<= 1

        if sink[i][j].bit_count() >= 2:
            result += 1
    print(result)
solution()
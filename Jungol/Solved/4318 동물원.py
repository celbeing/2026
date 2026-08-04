from collections import deque

def solution():
    h, w = map(int, input().split())
    cage = [[0] * w for _ in range(h)]
    foot_print = h*w
    for i in range(h):
        row = input().strip()
        for j in range(w):
            if row[j] == 'T': cage[i][j] = 1
            elif row[j] == 'B': cage[i][j] = -1
            else: foot_print -= 1

    result = 0
    d = [(1,0), (0,1), (-1,0), (0,-1)]
    stan = cage[0][0]
    check = [[0] * w for _ in range(h)]
    keep = [(0,0)]
    check[0][0] = 1
    bfs = deque()
    count = 0
    while True:
        while keep:
            bfs.append(keep.pop())

        while bfs:
            count += 1
            x, y = bfs.popleft()
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and check[nx][ny] == 0:
                    if cage[nx][ny] == stan:
                        bfs.append((nx, ny))
                        check[nx][ny] = 1
                    elif cage[nx][ny] == -stan:
                        keep.append((nx, ny))
                        check[nx][ny] = 1
        result += 1
        stan *= -1

        if count == foot_print: break
    print(result)

solution()
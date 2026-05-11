# backtracking

import sys
input = sys.stdin.readline

d = [(1,1),(1,-1),(-1,-1),(-1,1)]

def black_dfs(idx, cnt):
    if idx == black_count:
        global black_result
        if black_result < cnt:
            black_result = cnt
        return
    if check(black[idx]):
        bishop.add(black[idx])
        black_dfs(idx + 1, cnt + 1)
        bishop.discard(black[idx])

    if black_result < cnt + black_count - idx:
        black_dfs(idx + 1, cnt)
    return

def white_dfs(idx, cnt):
    if idx == white_count:
        global white_result
        if white_result < cnt:
            white_result = cnt
        return
    if check(white[idx]):
        bishop.add(white[idx])
        white_dfs(idx + 1, cnt + 1)
        bishop.discard(white[idx])

    if white_result < cnt + white_count - idx:
        white_dfs(idx + 1, cnt)
    return

def check(c):
    x, y = c
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        while 0<=nx<n and 0<=ny<n:
            if board[nx][ny] == '*': break

            if (nx, ny) in bishop:
                return False
            nx += dx
            ny += dy

    return True

for _ in range(int(input())):
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    black = []
    white = []
    black_count = 0
    white_count = 0
    black_result = 0
    white_result = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                if (i+j) & 1:
                    white.append((i, j))
                    white_count += 1
                else:
                    black.append((i, j))
                    black_count += 1
    bishop = set()
    black_dfs(0, 0)
    bishop.clear()
    white_dfs(0, 0)
    print(black_result + white_result)
from collections import deque

def zip(board):
    ret = 0
    for a in board:
        ret *= 10
        ret += a
    return ret

def piz(zip):
    board = []
    for _ in range(9):
        board.append(zip%10)
        zip //= 10
    board.reverse()
    return board


def solution():
    solved = 123456780
    puzzle = []
    d = [1,-1,3,-3]
    for _ in range(3):
        puzzle += list(input().split())
    state = dict()
    route = dict()
    s = -1
    for i in range(9):
        if puzzle[i] == 'X':
            puzzle[i] = 0
            s = i
        else:
            puzzle[i] = int(puzzle[i])

    bfs = deque()
    bfs.append((zip(puzzle),s))
    state[bfs[0][0]] = 0

    while bfs:
        org, x = bfs.popleft()
        if org == solved: break
        depth = state[org]
        now = piz(org)

        if x % 3 < 2:
            now[x], now[x + d[0]] = now[x + d[0]], now[x]
            next = zip(now)
            if not next in state:
                state[next] = depth+1
                route[next] = tuple((org, now[x]))
                bfs.append((next, x+d[0]))
            now[x], now[x + d[0]] = now[x + d[0]], now[x]

        if x % 3 > 0:
            now[x], now[x + d[1]] = now[x + d[1]], now[x]
            next = zip(now)
            if not next in state:
                state[next] = depth + 1
                route[next] = tuple((org, now[x]))
                bfs.append((next, x + d[1]))
            now[x], now[x + d[1]] = now[x + d[1]], now[x]

        if x < 6:
            now[x], now[x + d[2]] = now[x + d[2]], now[x]
            next = zip(now)
            if not next in state:
                state[next] = depth + 1
                route[next] = tuple((org, now[x]))
                bfs.append((next, x + d[2]))
            now[x], now[x + d[2]] = now[x + d[2]], now[x]

        if x > 2:
            now[x], now[x + d[3]] = now[x + d[3]], now[x]
            next = zip(now)
            if not next in state:
                state[next] = depth + 1
                route[next] = tuple((org, now[x]))
                bfs.append((next, x + d[3]))
            now[x], now[x + d[3]] = now[x + d[3]], now[x]

    if not solved in state: print(0)
    else:
        print(state[solved])
        res = []
        while solved in route:
            next, dir = route[solved]
            res.append(dir)
            solved = next
        res.reverse()
        print(*res)

solution()
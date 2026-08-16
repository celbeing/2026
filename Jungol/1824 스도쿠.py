def check(x, y, grid):
    row, col, box = set(), set(), set()
    for i in range(9):
        if grid[x][i]:
            if grid[x][i] in row:
                return 0
            row.add(grid[x][i])
        if grid[i][y]:
            if grid[i][y] in col:
                return 0
            col.add(grid[i][y])
    a, b = (x//3)*3, (y//3)*3
    for i in range(3):
        for j in range(3):
            p, q = a+i, b+j
            if grid[p][q]:
                if grid[p][q] in box:
                    return 0
                box.add(grid[p][q])
    return 1

def get_cand(x, y, grid):
    count = [0]*10
    for i in range(9):
        count[grid[x][i]] += 1
        count[grid[i][y]] += 1
    a, b = (x//3)*3, (y//3)*3
    for i in range(3):
        for j in range(3):
            p, q = a+i, b+j
            count[grid[p][q]] += 1

    res = []
    for i in range(1, 10):
        if count[i] == 0:
            res.append(i)
    return res

def dfs(k, grid):
    if k == 81:
        for a in grid:
            print(*a)
        exit()
    x, y = k//9, k%9
    if grid[x][y]:
        dfs(k+1, grid)
    cand = get_cand(x, y, grid)
    if cand:
        for i in cand:
            grid[x][y] = i
            if check(x, y, grid):
                dfs(k+1, grid)
        grid[x][y] = 0
    return

grid = [list(map(int, input().split())) for _ in range(9)]
dfs(0, grid)
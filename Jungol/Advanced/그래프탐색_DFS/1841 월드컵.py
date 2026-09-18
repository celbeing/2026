from itertools import permutations

def solution():
    a = list(map(int, input().split()))
    mat = [[0] * 6 for _ in range(6)]

    def dfs(x):
        if x == 6:
            return 1

        t = a[3*x:3*(x+1)]
        for i in range(x):
            if mat[x][i] == 1:
                t[0] -= 1
            elif mat[x][i] == 0:
                t[1] -= 1
            else:
                t[2] -= 1
        if t[0] < 0 or t[1] < 0 or t[2] < 0:
            return 0

        perm = [1]*t[0] + [0]*t[1] + [-1]*t[2]
        for p in set(permutations(perm, sum(t))):
            for y, k in enumerate(p, start=x+1):
                mat[x][y] = k
                mat[y][x] = -k
            return dfs(x+1)
        return 0
    print(dfs(0))


solution()
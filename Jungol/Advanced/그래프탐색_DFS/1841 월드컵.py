import sys
input = sys.stdin.readline

check = set()
res = [[0] * 6 for _ in range(6)]

def count():
    ret = [0] * 18
    for i in range(6):
        for j in range(i+1,6):
            if res[i][j] == 1:
                ret[i*3] += 1
                ret[j*3+2] += 1
            elif res[i][j] == 0:
                ret[i*3+1] += 1
                ret[j*3+1] += 1
            else:
                ret[i*3+2] += 1
                ret[j*3] += 1
    k = 0
    for a in ret:
        k *= 10
        k += a
    check.add(str(k))
    return

def dfs(i,j):
    a, b = i, j
    if b > 5:
        a += 1
        b = a+1
    if a == 5:
        count()
        return

    dfs(a,b+1)
    res[a][b] = 1
    res[b][a] = -1
    dfs(a,b+1)
    res[a][b] = -1
    res[b][a] = 1
    dfs(a,b+1)
    res[a][b] = 0
    res[b][a] = 0
    return

dfs(0,0)
ans = [0]*4
for i in range(4):
    a = input().strip().replace(' ','')
    if a in check:
        ans[i] = 1

print(*ans)
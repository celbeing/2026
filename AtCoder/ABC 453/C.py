import sys

n = int(input())
l = list(map(int, input().split()))
d = [1, -1]

res = 0
def dfs(now, cnt, depth):
    if depth == n:
        global res
        res = max(res, cnt)
        return

    for nd in d:
        next = now + l[depth] * nd
        if now*next < 0:
            dfs(next, cnt+1, depth+1)
        else:
            dfs(next, cnt, depth+1)

dfs(0.5, 0, 0)
print(res)
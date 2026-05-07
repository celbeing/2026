s = input().strip()
count = dict()
n = len(s)
for a in s:
    if a in count: count[a] += 1
    else: count[a] = 1

def dfs(now:str, depth:int):
    if depth == n: return 1

    ret = 0
    for next in count:
        if now == next or count[next] == 0: continue

        count[next] -= 1
        ret += dfs(next, depth+1)
        count[next] += 1

    return ret

print(dfs(' ', 0))
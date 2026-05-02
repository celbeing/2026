import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    road = [set() for _ in range(n+1)]
    for i in range(m):
        u, v = map(int, input().split())
        road[u].add(v)
        road[v].add(u)
    w = int(input())
    s = [''] + [list(input().strip()) for _ in range(n)]
    link = dict()
    for now in range(1, n+1):
        road[now].add(now)
        for d in range(w):
            if s[now][d] == 'o':
                link[(now,d)] = set()
                for next in road[now]:
                    if s[next][(d+1)%w] == 'o':
                        link[(now, d)].add((next, (d + 1) % w))

    flag = False
    for i in range(1, n+1):
        if s[i][0] == 'o':
            dfs = [(i,0)]
            check = set()
            check.add((i,0))
            while dfs:
                now = dfs.pop()
                for next in link[now]:
                    if next in check:
                        flag = True
                        dfs.clear()
                        break
                    else:
                        dfs.append(next)
                        check.add(next)
            if flag: break
    print('Yes' if flag else 'No')
import sys
from random import shuffle
from collections import deque
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    comp = [[0] * m for _ in range(n)]

    graph = [set()]

    d = [(1,0),(0,1),(-1,0),(0,-1)]
    count = 0
    for i in range(n):
        for j in range(m):
            if comp[i][j] == 0:
                graph.append(set())
                count += 1
                comp[i][j] = count
                bfs = deque([(i,j)])
                while bfs:
                    x, y = bfs.popleft()
                    for dx, dy in d:
                        nx, ny = x+dx, y+dy
                        if 0<=nx<n and 0<=ny<m:
                            if grid[nx][ny] == grid[x][y] and comp[nx][ny] == 0:
                                comp[nx][ny] = count
                                bfs.append((nx,ny))
                            elif 0 < comp[nx][ny] != count:
                                graph[count].add(comp[nx][ny])
                                graph[comp[nx][ny]].add(count)
    graph = [list(g) for g in graph]
    dist = [0] * (count+1)
    visit = [0] * (count+1)
    lower_bound = [-1] * (count+1)

    lower_bound[1] = 0
    bfs = deque([1])
    ecc = 0
    while bfs:
        now = bfs.popleft()
        for next in graph[now]:
            if lower_bound[next] == -1:
                lower_bound[next] = lower_bound[now]+1
                ecc = max(ecc, lower_bound[next])
                bfs.append(next)
    for i in range(1, count+1):
        lower_bound[i] = max(lower_bound[i], ecc-lower_bound[i])

    def radius(s, lm):
        dist[s] = 0
        visit[s] = s
        bfs = deque([s])
        ret = 0
        while bfs:
            now = bfs.popleft()
            for next in graph[now]:
                if visit[next] != s:
                    visit[next] = s
                    dist[next] = dist[now]+1
                    if dist[next] == lm:
                        return lm
                    else:
                        ret = max(ret, dist[next])
                    bfs.append(next)
        return ret

    result = n//2 + m//2
    search_order = [i for i in range(1, count+1)]
    shuffle(search_order)
    for i in search_order:
        if lower_bound[i] >= result: continue
        result = radius(i, result)
    print(result)
solution()
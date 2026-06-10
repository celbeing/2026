import sys
from math import ceil
from collections import deque
input = sys.stdin.readline

def solution():
    N, K = map(int, input().split()); K+=1
    airport = [(0,0),(10000,10000)]
    dist = [[0]*(N+2) for _ in range(N+2)]
    dist[0][1] = dist[1][0] = 1415
    for i in range(2, N+2):
        x, y = map(int, input().split())
        for j in range(i):
            dist[i][j] = dist[j][i] = ceil((((airport[j][0]-x)**2 + (airport[j][1]-y)**2)**0.5)/10)
        airport.append((x, y))

    def check(k):
        cost = [float('inf')]*(N+2)
        cost[0] = 0
        bfs = deque([0])
        while bfs:
            now = bfs.popleft()
            for next in range(1, N+2):
                if dist[now][next] <= k and cost[next] > cost[now]+1:
                    cost[next] = cost[now]+1
                    bfs.append(next)
        if cost[1] <= K: return True
        else: return False

    s, e = 2, 1415
    while s < e:
        m = (s + e) // 2
        if check(m):
            e = m
        else:
            s = m+1
    print(s)

solution()

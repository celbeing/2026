import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline

def solution():
    n = int(input())
    link = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        link[u].append(v)
        link[v].append(u)
    rank = [-1] * (n+1)
    income = [0] * (n+1)
    sub = [1] * (n+1)
    parent = [i for i in range(n+1)]

    rank[1] = 0
    bfs = deque([1])
    leaf = []
    while bfs:
        now = bfs.popleft()
        for next in link[now]:
            if rank[next] == -1:
                rank[next] = rank[now]+1
                parent[next] = now
                bfs.append(next)
                income[now] += 1
        if income[now] == 0:
            heappush(leaf, (-rank[now], now))

    while leaf:
        _, now = heappop(leaf)
        if now == 1: break
        sub[parent[now]] += sub[now]

        income[parent[now]] -= 1
        if income[parent[now]] == 0:
            heappush(leaf, (-rank[parent[now]], parent[now]))
    res = sum(rank[1:])*(n-1)
    for i in range(2, n+1):
        res -= sub[i]*(sub[i]-1)//2
    print(res)
solution()
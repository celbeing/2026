import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    code = dict()
    hd = [set() for _ in range(n+1)]

    for i in range(1,n+1):
        c = int('0b'+input().strip(), 2)
        code[c] = i
    for now in code:
        i = code[now]
        x = 1
        for j in range(k):
            p = now ^ x
            if p in code:
                hd[i].add(code[p])
            x <<= 1

    dist = [-1] * (n+1)
    head = [i for i in range(n+1)]
    dist[1] = 0
    bfs = deque([1])
    while bfs:
        now = bfs.popleft()
        for next in hd[now]:
            if dist[next] >= 0: continue
            dist[next] = dist[now] + 1
            head[next] = now
            bfs.append(next)
    m = int(input())
    for _ in range(m):
        j = int(input())
        if head[j] == j:
            print(-1)
            continue
        res = [j]
        while j > 1:
            res.append(head[j])
            j = head[j]
        print(*reversed(res))

solution()
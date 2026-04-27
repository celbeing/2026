import sys
from collections import deque
input = sys.stdin.readline

n, q = map(int, input().split())
road = [dict() for _ in range(n+1)]
robot = dict()
for _ in range(n-1):
    u, v, w = map(int, input().split())
    road[u][v] = w
    road[v][u] = w

parent = [i for i in range(n+1)]
depth = [-1] * (n+1)
dist_from_1 = [0] * (n+1)
branch_length = [0] * (n+1)
branch_from = [i for i in range(n+1)]
stem = set()

depth[1] = 0
bfs = deque([1])

while bfs:
    now = bfs.popleft()
    for nxt in road[now]:
        if depth[nxt] == -1:
            parent[nxt] = now
            depth[nxt] = depth[now]+1
            dist_from_1 = dist_from_1[now]+road[now][nxt]
            bfs.append(nxt)

stem.add(n)
idx = n
while idx > 1:
    idx = parent[idx]
    stem.add(idx)
    for nxt in road[idx]:
        if not(nxt in stem or nxt != parent[idx]):
            bfs.append(nxt)
            while bfs:
                pass
                # 대충 줄기가 아닌 지점들을 쭉 탐색해서
                # 줄기까지의 거리를 기록해두기
                # 나중에 로봇이 배치되면 줄기에 닿는지 확인하고,
                # 줄기에서 어느 범위를 커버할 수 있는지 O(1) 내에 확인할 수 있도록



for i in range(1,q+1):
    query = list(map(int, input().split()))
    if query[1] == 1:
        a, b = query[1:]

    else:
        c = query[1]
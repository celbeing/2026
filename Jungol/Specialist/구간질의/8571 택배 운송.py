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
dist_from_1 = [-1] * (n+1)
branch_length = [0] * (n+1)
branch_from = [0] * (n+1)
stem = set()

dist_from_1[1] = 0
bfs = deque([1])

while bfs:
    now = bfs.popleft()
    for nxt in road[now]:
        if dist_from_1[nxt] == -1:
            parent[nxt] = now
            dist_from_1[nxt] = dist_from_1[now]+road[now][nxt]
            bfs.append(nxt)

stem.add(n)
idx = n
while idx > 1:
    idx = parent[idx]
    stem.add(idx)
    branch_from[idx] = dist_from_1[idx]
    for nxt in road[idx]:
        if not(nxt in stem or nxt == parent[idx]):
            bfs.append(nxt)
            branch_length[nxt] = road[idx][nxt]
            branch_from[nxt] = dist_from_1[idx]
            while bfs:
                now = bfs.popleft()
                for nxt_brn in road[now]:
                    if nxt_brn in stem or branch_length[nxt_brn] > 0: continue
                    branch_length[nxt_brn] = branch_length[now] + road[now][nxt_brn]
                    branch_from[nxt_brn] = branch_from[now]

point_set = set()
robot = []
for i in range(1,q+1):
    query = list(map(int, input().split()))
    if query[1] == 1:
        a, b = query[1:]
        b -= branch_length[a]
        s, e = branch_from[a]-b, branch_from[a]+b
        if s < 0: s = 0
        if e > dist_from_1[n]: e = dist_from_1[n]
        if b <= 0:
            s, e = 0, 0
        point_set.add(s)
        point_set.add(e)
        robot.append((1, s, e))

    else:
        c = query[1]-1
        robot.append((-1, robot[c][1], robot[c][2]))

coor = dict()
for i, point in enumerate(sorted(list(point_set))):
    coor[point] = i

l = len(point_set)
size = 1
while size < l:
    size <<= 1

cover_seg = [0] * size * 2
count_seg = [0] * size * 2

for w, i, j in robot:
    i, j = i+size, j+size
    
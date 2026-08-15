from collections import deque

n = int(input())
parent = [i for i in range(n+1)]
child = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c = map(int, input().split())
    parent[c] = p
    child[p].append(c)

root = 0
for i in range(1, n+1):
    if parent[i] == i:
        root = i
        break

rank = [0] * (n+1)
rank[root] = 1
bfs = deque([root])

while bfs:
    now = bfs.popleft()
    for next in child[now]:
        rank[next] = rank[now] + 1
        bfs.append(next)

a, b = map(int, input().split())
while a != b:
    if rank[a] > rank[b]:
        a = parent[a]
    else:
        b = parent[b]
print(a)
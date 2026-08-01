n, m = map(int, input().split())
check = set()
graph = [set() for _ in range(n+1)]
x, y = map(int, input().split())
graph[x].add((x, y))
graph[y].add((x, y))
check.add((x, y))
count = 0
for _ in range(1, m):
    a, b = map(int, input().split())
    graph[a].add((a, b))
    graph[b].add((a, b))
    if (a, b) in check:
        count += 1
    check.add((a, b))

m -= count

count = 0
for i in range(1, n+1):
    if i == x or i == y: continue
    if len(graph[x] | graph[i]) == m:
        count += 1
    if len(graph[i] | graph[y]) == m:
        count += 1

if len(graph[x] | graph[y]) == m:
    count += 1
print(count)
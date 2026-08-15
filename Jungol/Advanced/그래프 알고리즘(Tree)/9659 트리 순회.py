from collections import deque

n = int(input())
parent = [i for i in range(1001)]
link = [[] for _ in range(1001)]
for _ in range(n-1):
    c, p = map(int, input().split())
    parent[c] = p
    link[c].append(p)
    link[p].append(c)
x = int(input())

def depth(node):
    ret = 0
    while node != 1:
        ret += 1
        node = parent[node]
    return ret

def dfs(now):
    ret = 1
    if link[now]:
        for next in link[now]:
            if next != parent[now]:
                ret += dfs(next)
    return ret

def far_cid(node):
    bfs = deque([(node, 0)])
    now = node
    far = 0
    while bfs:
        now, dep = bfs.popleft()
        far = dep
        for next in link[now]:
            if next != parent[now]:
                bfs.append((next, dep+1))
    return far

def far_node(node):
    bfs = deque([node])
    check = [0] * 1001
    now = node
    check[node] = 1
    while bfs:
        now = bfs.popleft()
        for next in link[now]:
            if check[next] == 0:
                bfs.append(next)
                check[next] = check[now] + 1
    return check[now] - 1

print(depth(x))
print(dfs(x))
print(far_cid(x))
print(far_node(x))
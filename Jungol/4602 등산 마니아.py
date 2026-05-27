import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

n = int(input())
link = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    link[u].append(v)
    link[v].append(u)
parent = [0] * (n+1)
child = [[] for _ in range(n+1)]
subtree = [1] * (n+1)
depth = [-1] * (n+1)
result = 0

def dfs(now, d):
    depth[now] = d
    for next in link[now]:
        if depth[next] == -1:
            parent[next] = now
            child[now].append(next)
            subtree[now] += dfs(next,d+1)
    return subtree[now]

dfs(1, 0)
for i in range(1, n+1):
    result += depth[i]*n - subtree[i]*depth[i]
    for c in child[i]:
        result -= (subtree[i]-subtree[c]-1)*subtree[c]

print(result)
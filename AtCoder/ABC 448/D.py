import sys
input = sys.stdin.readline
sys.setrecursionlimit(200001)

n = int(input())
a = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

check = [0] * (n + 1)
result = [1] * (n + 1)
path = set()
path.add(a[1])
check[1] = 1
result[1] = 0

def DFS(now):
    for nxt in tree[now]:
        if check[nxt]: continue
        check[nxt] = 1
        if not a[nxt] in path:
            result[nxt] = 0
            path.add(a[nxt])
            DFS(nxt)
    path.remove(a[now])
    return

check[1] = 1
DFS(1)

for k in range(1, n + 1):
    print('Yes' if result[k] else 'No')
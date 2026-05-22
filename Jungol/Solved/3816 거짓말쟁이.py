import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(range(n+1))
diff = [0] * (n+1)
rank = [0] * (n+1)

def find(x):
    if parent[x] != x:
        root = find(parent[x])
        diff[x] ^= diff[parent[x]]
        parent[x] = root
    return parent[x]

def union(a, b, w):
    ra = find(a)
    rb = find(b)
    pa = diff[a]
    pb = diff[b]

    if ra == rb:
        return pa^pb == w

    if rank[ra] < rank[rb]:
        parent[ra] = rb
        diff[ra] = pa^pb^w
    else:
        parent[rb] = ra
        diff[rb] = pa^pb^w
        if rank[ra] == rank[rb]:
            rank[ra] += 1
    return True

for i in range(m):
    x, y, w = input().split()
    x, y = int(x), int(y)
    w = 0 if w == 'T' else 1
    if not union(x, y, w):
        print(i)
        break
else:
    print(m)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
head = [i for i in range(n + 1)]
count = [1] * (n+1)

def find(k):
    t = k
    while head[t] != t:
        t = head[t]
    head[k] = t
    return t

def union(a, b):
    A = find(a)
    B = find(b)
    if A < B:
        head[B] = A
        count[A] += count[B]
    elif A > B:
        head[A] = B
        count[B] += count[A]

for _ in range(m):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x, y = q[1:]
        union(x,y)
    else:
        x = q[1]
        print(count[find(x)])
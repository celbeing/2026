import sys
input = sys.stdin.readline

def solution():
    n, m, k = map(int, input().split())
    link = [tuple(map(int, input().split())) for _ in range(m)]
    link.reverse()
    count = n
    parent = [i for i in range(n+1)]

    def find(x):
        t = x
        while parent[t] != t:
            t = parent[t]
        parent[x] = t
        return t

    def union(a, b):
        A = find(a)
        B = find(b)
        if A == B: return 0

        if A < B:
            parent[B] = A
        else:
            parent[A] = B
        return 1
    if k == 1:
        print(0)
    else:
        for i, (a, b) in enumerate(link):
            count -= union(a, b)
            if count < k:
                print(m-i)
                break

solution()
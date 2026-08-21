import sys
input = sys.stdin.readline

def solution():
    n, q = map(int, input().split())
    parent = [0, 1] + [int(input()) for _ in range(n-1)]
    head = [i for i in range(n+1)]

    def find(k):
        t = k
        while head[t] != t:
            t = head[t]
        head[k] = t
        return t

    query = [tuple(map(int, input().split())) for _ in range(n-1+q)]
    query.reverse()
    res = []
    for q in query:
        if q[0] == 0:
            b = q[1]
            head[b] = find(parent[b])
        else:
            a, b = q[1], q[2]
            res.append("YES" if find(a) == find(b) else "NO")
    res.reverse()
    print('\n'.join(res))
solution()
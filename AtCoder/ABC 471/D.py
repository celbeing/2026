import sys
input = sys.stdin.readline
from heapq import heappush, heappop

q, v = map(int, input().split())
slot = []
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        t, w = query[1:]
        heappush(slot, t-w)
    else:
        t = query[1]
        if slot:
            ch = -heappop(slot)+t
            if ch > v: ch = v
            print(ch)
        else:
            print(-1)
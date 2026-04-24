# priority_queue

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

res, cnt = 0, 0
n, k = map(int, input().split())
cash = [(0,0,i) for i in range(k)]

for _ in range(n):
    id, w = map(int, input().split())
    now_time = cash[0][0]
    outline = []

    while cash and cash[0][1] and cash[0][0] == now_time:
        t,o,c = heappop(cash)
        outline.append((c,o))

    outline.sort()
    while outline:
        c, o = outline.pop()
        if o:
            cnt += 1
            res += cnt * o
        heappush(cash, (now_time, 0, c))

    time, out, casher = heappop(cash)
    heappush(cash, (time+w, id, casher))

while cash:
    now_time = cash[0][0]
    outline = []
    while cash and cash[0][0] == now_time:
        t,o,c = heappop(cash)
        outline.append((c,o))
    outline.sort()
    while outline:
        c, o = outline.pop()
        if o:
            cnt += 1
            res += cnt * o
print(res)
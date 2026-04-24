# priority_queue, hash_set

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

ugly = [0, 1]
check = set()
hq = [2, 3, 5]
check.update(hq)
cnt = 1
while cnt < 1501:
    now = heappop(hq)
    ugly.append(now)
    for k in (2, 3, 5):
        if now * k in check:
            continue
        check.add(now * k)
        heappush(hq, now * k)
    cnt += 1
while True:
    n = int(input())
    if n == 0: break
    print(ugly[n])
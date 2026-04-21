import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())
top, btm = [], []
heappush(top, int(input()))
print(top[0])
for _ in range(n//2):
    a, b, = map(int, input().split())
    if top[0] < a:
        heappush(btm, -heappop(top))
        heappush(top, a)
    else:
        heappush(btm, -a)

    if -btm[0] > b:
        heappush(top, -heappop(btm))
        heappush(btm, -b)
    else:
        heappush(top, b)

    print(top[0])
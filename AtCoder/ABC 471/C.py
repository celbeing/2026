import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
a = list(map(int, input().split()))
p, m = [], []
for k in a:
    if k > 0:
        heappush(p, k)
    else:
        heappush(m, -k)

move = 0
now = 0
while p and m:
    if p[0]-now < m[0]+now:
        move += p[0]-now
        now = heappop(p)
    else:
        move += m[0]+now
        now = -heappop(m)
while p:
    move += p[0]-now
    now = heappop(p)
while m:
    move += m[0]+now
    now = -heappop(m)
print(move)
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())
a, b = map(int, input().split())
x-=1;y-=1;a-=1;b-=1
l = list(map(int, input().split()))
count = dict()
count[(x, y)] = 0
hq = [(0,x,y)]
while hq:
    d, i, j = heappop(hq)
    if count[(i, j)] < d: continue
    if i == a:
        if j == b: break
        if not (a, b) in count or count[(a, b)] > d+abs(j-b):
            count[(a, b)] = d+abs(j-b)
            heappush(hq, (d+abs(j-b),a,b))
    if j == 0 and i > 0:
        ni, nj = i-1, l[i-1]
        if not (ni, nj) in count or count[(ni, nj)] > d+1:
            count[(ni, nj)] = d+1
            heappush(hq, (d+1,ni,nj))
    if j == l[i] and i < n-1:
        ni, nj = i+1, 0
        if not (ni, nj) in count or count[(ni, nj)] > d+1:
            count[(ni, nj)] = d+1
            heappush(hq, (d+1,ni,nj))
    if not (i, 0) in count or count[(i, 0)] > d+j:
        count[(i, 0)] = d+j
        heappush(hq, (d+j, i, 0))
    if not (i, l[i]) in count or count[(i, l[i])] > d+l[i]-j:
        count[(i, l[i])] = d+l[i]-j
        heappush(hq, (d+l[i]-j,i,l[i]))
    if i > 0:
        ni, nj = i-1, min(j, l[i-1])
        if not (ni, nj) in count or count[(ni, nj)] > d+1:
            count[(ni, nj)] = d+1
            heappush(hq, (d+1,ni,nj))
    if i < n-1:
        ni, nj = i+1, min(j, l[i+1])
        if not (ni, nj) in count or count[(ni, nj)] > d+1:
            count[(ni, nj)] = d+1
            heappush(hq, (d+1,ni,nj))
print(count[(a, b)])
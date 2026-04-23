import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = dict()
s, e = 0, 1
min_hq, max_hq = [a[0]], [-a[0]]
cnt[a[0]] = 1
res = 1

while e < n:
    heappush(min_hq, a[e])
    heappush(max_hq, -a[e])
    if a[e] in cnt:
        cnt[a[e]] += 1
    else:
        cnt[a[e]] = 1
        while min_hq[0]+max_hq[0] < -k:
            if cnt[a[s]] == 1:
                del cnt[a[s]]
                while not (min_hq[0] in cnt):
                    heappop(min_hq)
                while not(-max_hq[0] in cnt):
                    heappop(max_hq)
            else:
                cnt[a[s]] -= 1
            s += 1
    res = max(res, e-s+1)
    e += 1
print(res)
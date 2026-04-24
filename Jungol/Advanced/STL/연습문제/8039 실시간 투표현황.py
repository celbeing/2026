# hash_set

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
vote = dict()
cand = dict()
vote[0] = set()
vote[0].update([i for i in range(1, N+1)])
for i in range(1, N+1):
    cand[i] = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        n, k = query[1], query[2]
        vote[cand[n]].discard(n)
        cand[n] += k
        if not(cand[n] in vote):
            vote[cand[n]] = set()
        vote[cand[n]].add(n)

    else:
        x = query[1]
        if x in vote and len(vote[x]):
            print(*sorted(vote[x]))
        else:
            print('None')
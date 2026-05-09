import sys
from collections import deque
input = sys.stdin.readline

a, b, c, d = map(int, input().split())
check = set()
check.add((0,0))
bfs = deque([(0,0,0)])
while bfs:
    cnt, na, nb = bfs.popleft()
    if na == c and nb == d:
        print(cnt)
        break
    if not (a, nb) in check:
        check.add((a, nb))
        bfs.append((cnt+1, a, nb))
    if not (na, b) in check:
        check.add((na, b))
        bfs.append((cnt+1, na, b))
    if a-na >= nb and not (na+nb, 0) in check:
        check.add((na+nb, 0))
        bfs.append((cnt+1, na+nb, 0))
    else:
        k = a-na
        if nb >= k and not (a, nb-k) in check:
            check.add((a, nb-k))
            bfs.append((cnt+1,a,nb-k))
    if b-nb >= na and not (0, na+nb) in check:
        check.add((0, na+nb))
        bfs.append((cnt+1, 0, na+nb))
    else:
        k = b-nb
        if na >= k and not (na-k, b) in check:
            check.add((na-k, b))
            bfs.append((cnt+1,na-k,b))
    if not (0, nb) in check:
        check.add((0, nb))
        bfs.append((cnt+1,0,nb))
    if not (na, 0) in check:
        check.add((na, 0))
        bfs.append((cnt+1,na,0))
else:
    print(-1)
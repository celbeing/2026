from collections import deque

def solution():
    x, y, k = map(int, input().split())
    bfs = deque([(y, 1, 0)])
    while bfs:
        l, r, dep = bfs.popleft()
        if l<=x<l+r:
            return dep

        if r == 1:
            bfs.append((l//k, 1, dep+1))
        bfs.append((l*k, r*k, dep+1))

    return 0

for _ in range(int(input())):
    print(solution())
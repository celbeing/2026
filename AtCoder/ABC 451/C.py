import sys
from heapq import heappush, heappop
input = sys.stdin.readline
tree = []
for _ in range(int(input())):
    q, h = map(int, input().split())
    if q == 1:
        heappush(tree, h)
    else:
        while tree and tree[0] <= h:
            heappop(tree)
    print(len(tree))

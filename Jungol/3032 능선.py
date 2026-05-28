import sys
from heapq import heappush, heappop
from collections import deque
input = sys.stdin.readline

h, w = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]

hq = []
for i in range(h):
    for j in range(w):
        heappush(hq, (-grid[i][j],i,j))

# 물줄기 갈라졌다가 합쳐지는거 어떻게 판단하지?
while hq
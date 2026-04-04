import sys
input = sys.stdin.readline
h,w = map(int, input().split())
grid = [['.']* w for _ in range(h)]
for i in range(w):
    grid[0][i] = '#'
    grid[-1][i] = '#'
for i in range(h):
    grid[i][0] = '#'
    grid[i][-1] = '#'

for line in grid:
    print(''.join(line))
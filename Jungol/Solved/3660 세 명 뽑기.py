import sys
input = sys.stdin.readline

n = int(input())
grid = [[0] * n for _ in range(n)]
for i in range(n-1):
    line = list(map(int, input().split()))
    for j, l in enumerate(line):
        grid[i][i+j+1] = l
        grid[i+j+1][i] = l
res = n*(n-1)*(n-2)//6
neg = 0
for i in range(n):
    f = sum(grid[i])
    neg += (n-1-f)*f
print(res-neg//2)
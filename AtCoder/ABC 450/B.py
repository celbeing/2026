import sys
input = sys.stdin.readline
n = int(input())
inf = int(1e12)
cost = [[inf] * n for _ in range(n)]
for i in range(n):
    j = i + 1
    c = list(map(int, input().split()))
    for k in c:
        cost[i][j] = k
        j += 1
flag = False
for i in range(n - 2):
    for j in range(i + 2, n):
        for k in range(i + 1, j):
            if cost[i][j] > cost[i][k] + cost[k][j]:
                flag = True

print('Yes' if flag else 'No')
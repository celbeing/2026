import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    dist = []
    for i in range(n - 1):
        dist.append([0] * (i+1) + list(map(int, input().split())))
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if dist[i][j] + dist[i][k] == dist[j][k]:
                    continue
                elif dist[i][j] + dist[j][k] == dist[i][k]:
                    continue
                elif dist[i][j] == dist[i][k] + dist[j][k]:
                    continue
                else:
                    print('No')
                    return
    print('Yes')
    return

solution()
import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n = int(input())
    link = [[] for _ in range(n+1)]
    parent = [i for i in range(n+1)]
    children = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        link[u].append(v)
        link[v].append(u)

    dfs = [1]
    # 최대 독립집합 필수 정점 찾기
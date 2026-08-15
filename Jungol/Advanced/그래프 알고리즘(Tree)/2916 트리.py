import sys
input = sys.stdin.readline
from collections import deque

def solution():
    n = int(input())
    tree = [dict() for _ in range(n)]
    parent
    for i in range(1, n):
        tree[i][0] = 0
        tree[0][i] = 0
    print(sys.getsizeof(tree))

solution()
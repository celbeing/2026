import sys
from collections import deque
input = sys.stdin.readline

def ccw(a, b, c):
    k = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])
    if k > 0: return -1
    elif k < 0: return 1
    else: return 0

def graham(dots):
    dots.sort()
    left = []
    right = []
    for p in dots:
        while len(left) >= 2 and ccw(left[-2],left[-1],p) <= 0:
            left.pop()
        left.append(p)
    for p in reversed(dots):
        while len(right) >= 2 and ccw(right[-2],right[-1],p) <= 0:
            right.pop()
        right.append(p)

    return left[:-1]+right[:-1]

while True:
    n = int(input())
    if n == 0: break

    dot = [tuple(map(int, input().split())) for _ in range(n)]
    hull = graham(dot)

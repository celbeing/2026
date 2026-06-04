import sys
from math import ceil
input = sys.stdin.readline

def ccw(a, b, c):
    k = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])
    if k > 0: return -1
    elif k < 0: return 1
    else: return 0

def dist(a, b, c):
    if b == c:
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
    p = abs((c[0]-b[0])*(a[1]-b[1])-(c[1]-b[1])*(a[0]-b[0]))
    q = ((c[0]-b[0])**2 + (c[1]-b[1])**2)**0.5
    return p/q

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

    return left[:-1] + right[:-1]

t = 1
while True:
    n = int(input())
    if n == 0: break

    dot = [tuple(map(int, input().split())) for _ in range(n)]
    hull = graham(dot)
    edge = len(hull)
    result = float('inf')
    for i in range(edge):
        j, k = (i+1)%edge, (i+2)%edge
        size = 0
        while k != i:
            size = max(size, dist(hull[k],hull[i],hull[j]))
            k += 1
            k %= edge
        result = min(result, size)
    result = ceil(result*100 - 1e-9)/100
    print(f'Case {t}: {result:.2f}')
    t += 1

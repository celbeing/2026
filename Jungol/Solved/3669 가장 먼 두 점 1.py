import sys
input = sys.stdin.readline

def ccw(a, b, c):
    k = cross(a, b, c)
    if k > 0: return -1
    elif k < 0: return 1
    else: return 0

def cross(a, b, c):
    return (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])

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

def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def rotating_calipers(hull):
    n = len(hull)
    if n == 2:
        return dist(hull[0], hull[1])

    ret = 0
    j = 1
    for i in range(n):
        p = (i+1)%n
        while True:
            q = (j+1)%n
            now = abs(cross(hull[i], hull[p], hull[j]))
            next = abs(cross(hull[i], hull[p], hull[q]))

            if now < next:
                j = q
            else:
                break
        ret = max(ret, dist(hull[i], hull[j]), dist(hull[p], hull[j]))

    return ret

def solution():
    n = int(input())
    dot = [tuple(map(int, input().split())) for _ in range(n)]
    hull = graham(dot)
    print(rotating_calipers(hull))

solution()
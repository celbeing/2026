import sys
input = sys.stdin.readline

def ccw(a, b, c):
    k = cross(a, b, c)
    if k > 0: return -1
    elif k < 0: return 1
    else: return 0

def cross(a, b, c):
    return (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])

def area(a, b, c):
    return abs((a[0]*b[1]+b[0]*c[1]+c[0]*a[1])-(a[1]*b[0]+b[1]*c[0]+c[1]*a[0]))/2

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
    if n < 3:
        return 0

    dots = hull*3
    j, k = 1, 2
    ret = 0
    for i in range(n):
        if j <= i: j = i + 1
        if k <= j: k = j + 1

        while True:
            flag = False
            while k+1 < i+n and area(dots[i], dots[j], dots[k+1]) >= area(dots[i], dots[j], dots[k]):
                k += 1
                flag = True
            while j+1 < k and area(dots[i], dots[j+1], dots[k]) >= area(dots[i], dots[j], dots[k]):
                j += 1
                flag = True
            if not flag: break
        ret = max(ret, area(dots[i], dots[j], dots[k]))

    return ret

def solution():
    n = int(input())
    dot = [tuple(map(int, input().split())) for _ in range(n)]
    hull = graham(dot)
    print(f'{rotating_calipers(hull):.2f}')

solution()
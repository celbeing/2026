import sys
input = sys.stdin.buffer.readline

def cross(a, b, c):
    return (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])

def graham(dots):
    dots.sort()
    left = []
    right = []
    for p in dots:
        while len(left) >= 2 and cross(left[-2],left[-1],p) <= 0:
            left.pop()
        left.append(p)
    for p in reversed(dots):
        while len(right) >= 2 and cross(right[-2],right[-1],p) <= 0:
            right.pop()
        right.append(p)

    hull = left[:-1] + right[:-1]
    n = len(hull)
    if n == 2:
        return dist(hull[0], hull[1])

    ret = 0
    j = 1
    for i in range(n):
        p = (i + 1) % n
        while True:
            q = (j + 1) % n
            now = abs(cross(hull[i], hull[p], hull[j]))
            next = abs(cross(hull[i], hull[p], hull[q]))

            if now < next:
                j = q
            else:
                break
        ret = max(ret, dist(hull[i], hull[j]), dist(hull[p], hull[j]))

    return ret

def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def solution():
    n, t = map(int, input().split())
    stars =[tuple(map(int, input().split())) for _ in range(n)]
    memo = dict()

    def k_date(k):
        if k in memo: return memo[k]
        now = []
        for x, y, dx, dy in stars:
            now.append((x+dx*k, y+dy*k))
        ret = graham(now)
        memo[k] = ret
        return ret

    s, e = 0, t
    while e - s > 5:
        m1 = s + (e-s)//3
        m2 = e - (e-s)//3
        if k_date(m1) <= k_date(m2):
            e = m2-1
        else:
            s = m1+1
    res1 = s
    res2 = k_date(s)
    for i in range(s, e+1):
        cnt = k_date(i)
        if cnt < res2:
            res1 = i
            res2 = cnt
    print(res1)
    print(res2)

solution()
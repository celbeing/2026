def solution(p, q, r, s):
    x1 = q[0]-p[0]
    x2 = s[0]-r[0]
    y1 = q[1]-p[1]
    y2 = s[1]-r[1]

    x3 = r[0]+s[0]-p[0]-q[0]
    y3 = r[1]+s[1]-p[1]-q[1]

    if x1*y2 - x2*y1:
        print('Yes')
    elif x1*x3 + y1*y3:
        print('No')
    else:
        print('Yes')

t = int(input())
for _ in range(t):
    d = list(map(int, input().split()))
    solution(d[:2], d[2:4], d[4:6], d[6:])
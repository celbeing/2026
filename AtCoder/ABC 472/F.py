n, q = map(int, input().split())
p = [tuple(map(int, input().split())) for _ in range(n)]
p.append(p[0])

def ccw(p1, p2, p3):
    k = (p1[1]-p2[1])*(p2[0]-p3[0])-(p1[0]-p2[0])*(p2[1]-p3[1])
    if k > 0:
        return 1
    elif k < 0:
        return -1
    else:
        return 0

def get_cent(poly):
    n = len(poly)
    area = 0
    x, y = 0, 0
    for i in range(n):
        x0, y0 = poly[i]
        x1, y1 = poly[(i+1)%n]

        cross = (x0*y1)-(x1*y0)
        area += cross
        x += (x0+x1)*cross
        y += (y0+y1)*cross
    x /= area*3
    y /= area*3
    print(x, y)
    return

def query():
    u, v = map(int, input().split())

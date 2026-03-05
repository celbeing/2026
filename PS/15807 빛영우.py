import sys
input = sys.stdin.readline

def rotate(x, y):
    nx = (x + y) ** 2
    ny = (-x + y) ** 2
    return nx, ny

def solution():
    dots = []
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        nx, ny = rotate(x, y)
        dots.append((nx, ny, -1))

    yh = dict()
    p = int(input())
    res = [0] * p
    for i in range(p):
        x, y = map(int, input().split())
        nx, ny = rotate(x, y)
        dots.append((nx, ny, i))
        yh[(nx, ny)] = i

    dots.sort()
    light = 0
    for x, y, o in dots:
        if o == -1:
            light += 1
        else:
            n = yh[(x, y)]
            res[n] = light

    for k in res:
        print(k)

solution()
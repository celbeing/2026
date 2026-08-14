def solution():
    x, y, h = map(float, input().split())
    x = int(x*10000)
    y = int(y*10000)
    h = int(h*10000)

    s, e = 0, min(x, y)
    while s < e:
        m = (s+e)//2
        t = (1/((x**2-m**2)**0.5))+(1/((y**2-m**2)**0.5))
        if 1/h == t:
            s = m
            break
        elif 1/h < t: e = m
        else: s = m+1
    s += 5
    s //= 10
    s /= 1000
    print(s)
solution()
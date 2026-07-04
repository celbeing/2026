x, y, l, r, a, b = map(int, input().split())
res = 0
if a < l:
    res += (l-a)*y
    if b <= l:
        res -= (l-b)*y
    elif b <= r:
        res += (b-l)*x
    else:
        res += (r-l)*x
        res += (b-r)*y
elif a <= r:
    res += (r-a)*x
    if b <= r:
        res -= (r-b)*x
    else:
        res += (b-r)*y
else:
    res += (b-a)*y
print(res)
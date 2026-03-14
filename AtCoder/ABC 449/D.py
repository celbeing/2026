l, r, d, u = map(int, input().split())
if r <= 0:
    l, r = -r, -l
if u <= 0:
    d, u = -u, -d

def count(x, y):
    p = min(x, y)
    if p < 1: return 0
    p //= 2
    ret = p * p * 2 + p

    p = min(x, y)
    q = max(x, y)
    if p % 2: p -= 1
    if q % 2: q -= 1

    ret += ((q - p) // 2) * min(x, y)
    return ret

res = 0

k = 0
res += count(r, u)

if l <= 0:
    res += count(-l, u)
else:
    res -= count(l - 1, u)

if d <= 0:
    res += count(r, -d)
else:
    res -= count(r, d - 1)

if l <= 0:
    if d <= 0:
        res += count(-l, -d)
    else:
        res -= count(-l, d - 1)
else:
    if d <= 0:
        res -= count(l - 1, -d)
    else:
        res += count(l - 1, d - 1)


if l <= 0:
    res += u // 2
    if d > 0:
        res -= (d - 1) // 2
    else:
        res += abs(d) // 2

if d <= 0:
    res += r // 2
    if l > 0:
        res -= (l - 1) // 2
    else:
        res += abs(l) // 2

if l <= 0 and d <= 0:
    res += 1

print(res)
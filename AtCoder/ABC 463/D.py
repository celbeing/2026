n, k = map(int, input().split())
cloth = [tuple(map(int, input().split())) for _ in range(n)]
cloth.sort(key=lambda x:(x[1]))

def count(d):
    res, end = 0, -d
    for l, r in cloth:
        if l - end >= d:
            end = r
            res += 1
    return res

ans = 0
s, e = 0, 1_000_000_000
while s < e:
    m = (s+e) // 2
    if count(m) >= k:
        ans = m
        s = m+1
    else:
        e = m
if ans == 0:
    ans = -1
print(ans)
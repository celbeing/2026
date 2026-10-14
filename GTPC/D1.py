n, m = map(int, input().split())
w = list(map(int, input().split()))

l, r = [], []
for k in w:
    if k < 0: l.append(-k)
    else: r.append(k)
l.sort()
r.sort()

res = 0
while res < len(l) and l[res] <= m:
    if l[res] <= m: res += 1

left = res - 1
right = 0
while left >= 0:
    while right < len(r) and l[left]+r[right]*2 <= m:
        right += 1
    res = max(res, left+right+1)
    left -= 1

left, right = 0, 0
while right < len(r) and r[right] <= m:
    if r[right] <= m: right += 1
res = max(res, right)
right -= 1
while right >= 0:
    while left < len(l) and r[right]+l[left]*2 <= m:
        left += 1
    res = max(res, left+right+1)
    right -= 1

print(res)
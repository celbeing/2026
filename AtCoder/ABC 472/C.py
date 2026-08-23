n, m, k = map(int, input().split())
a = list(map(int, input().split()))
check = [0] * n
pre = 0
l, r = 0, 0
res = []
while r < m:
    if pre+a[r] <= k:
        check[r] = 1
        pre += a[r]
        res.append('Yes')
    else:
        res.append('No')
    r += 1

while r < n:
    if check[l]:
        pre -= a[l]
    if pre+a[r] <= k:
        check[r] = 1
        pre += a[r]
        res.append('Yes')
    else:
        res.append('No')
    r += 1
    l += 1

print('\n'.join(res))
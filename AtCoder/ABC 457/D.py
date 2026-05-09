n, k = map(int, input().split())
a = list(map(int, input().split()))
s, e = min(a), a[0] + k
while s < e:
    m = (s+e+1)//2
    cnt = 0
    for i in range(n):
        if a[i] < m:
            cnt += (m-a[i])//(i+1) + (1 if (m-a[i])%(i+1) else 0)
        if cnt > k: break

    if cnt > k:
        e = m - 1
    else:
        s = m

print(s)
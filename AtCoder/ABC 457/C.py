n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = list(map(int, input().split()))
i = 0
while k > a[i][0] * c[i]:
    k -= a[i][0]*c[i]
    i += 1
k %= a[i][0]
if k == 0: k += a[i][0]
print(a[i][k])
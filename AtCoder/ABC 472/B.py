n = int(input())
l = list(map(int, input().split()))
a, b = 0, sum(l)
res = b
for k in l:
    a += k
    b -= k
    res = min(res, abs(a-b))
print(res)
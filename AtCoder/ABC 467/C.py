n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x, y = 0, 1
for i in range(1, n):
    if b[i-1]:
        if (a[i-1]+a[i])&1:
            y += 1
        else:
            x, y = y, x+1
    else:
        if (a[i-1]+a[i])&1:
            x, y = y, x+1
        else:
            y += 1
print(min(x, y))
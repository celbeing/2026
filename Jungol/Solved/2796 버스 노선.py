import io
input = io.BufferedReader(io.FileIO(0), 1 << 18).readline

n = int(input())
m = int(input())
bus = []
for i in range(1, m+1):
    a, b = map(int, input().split())
    if a > b:
        bus.append((a-n, b, i))
        bus.append((a, b+n, i))
    else:
        bus.append((a, b, i))

bus.sort(key=lambda x:(-x[1], x[0]))
check = [-1] * (m+1)
l, r = n, n*2
for a, b, i in bus:
    if check[i] == -1:
        if a < l:
            check[i] = 1
            l, r = a, b
        else:
            check[i] = 0
    elif check[i] == 1:
        l, r = a, b

res = []
for i in range(1, m+1):
    if check[i]: res.append(i)

print(*res)
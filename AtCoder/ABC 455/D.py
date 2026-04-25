n, q = map(int, input().split())

head = [i for i in range(n+1)]
foot = [i for i in range(n+1)]
for _ in range(q):
    c, p = map(int, input().split())
    if foot[c] != c:
        head[foot[c]] = foot[c]
    head[p] = c
    foot[c] = p

count = [0] * (n+1)

for i in range(1, n+1):
    if foot[i] == i:
        k = i
        count[i] += 1
        while head[k] != k:
            count[i] += 1
            k = head[k]

print(*count[1:])
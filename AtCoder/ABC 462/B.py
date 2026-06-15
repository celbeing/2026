n = int(input())
count = [0] * (n+1)
gift = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    a = list(map(int, input().split()))[1:]
    for t in a:
        count[t] += 1
        gift[t][i] = 1

for i in range(1, n+1):
    res = [count[i]]
    for j in range(1, n+1):
        if gift[i][j]:
            res.append(j)
    print(*res)
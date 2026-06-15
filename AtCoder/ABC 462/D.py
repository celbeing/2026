n, d = map(int, input().split())

check = [0] * 1000002
for _ in range(n):
    s, e = map(int, input().split())
    e -= d - 1
    if s < e:
        check[s] += 1
        check[e] -= 1

count = 0
result = 0

for i in range(1, 1000001):
    count += check[i]
    result += count*(count-1)//2

print(result)
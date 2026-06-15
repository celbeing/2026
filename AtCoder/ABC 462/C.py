n = int(input())
dot = [tuple(map(int, input().split())) for _ in range(n)]
dot.sort()
cnt = 0
low = 300000

count = 0
for x, y in dot:
    if y <= low:
        count += 1
        low = y
print(count)
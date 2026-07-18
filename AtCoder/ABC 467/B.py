n = int(input())
res = 0
for _ in range(n):
    a, b, s = input().split()
    if s == 'keep':
        res += int(b)-int(a)
print(res)
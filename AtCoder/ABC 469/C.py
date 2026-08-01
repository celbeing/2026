n = int(input())
s = input().strip()

r = -1
for l in range(n):
    if r < n-1:
        r += 1
    while r < n-1 and s[r] == 'o':
        r += 1
    print(r+1)
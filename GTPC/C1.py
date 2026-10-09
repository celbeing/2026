n = int(input())
res = 0
for i in range(1, n//4+1):
    for j in range(i, (n-i)//3+1):
        l = max(j, n//2-i-j+1)
        r = (n-i-j)//2
        if l<=r:
            res += r-l+1

print(res)
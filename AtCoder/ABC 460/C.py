import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
i,j,res = 0,0,0
while i < n and j < m:
    if b[j] > a[i]*2:
        i += 1
    else:
        res += 1
        i += 1
        j += 1
print(res)
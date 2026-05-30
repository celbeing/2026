import sys
input = sys.stdin.readline

n = int(input())
friend = [0]*n
for i in range(n-1):
    l = input().strip().replace(' ','')
    for k, s in enumerate(l):
        j = i+k+1
        if s == '1':
            friend[i] |= 1 << j
            friend[j] |= 1 << i

mask = (1<<n)-1
not_friend = [mask^friend[i]^(1<<i)for i in range(n)]

res = 0
for i in range(n-1):
    for j in range(i+1,n):
        if (friend[i]>>j) & 1:
            res += (friend[i] & friend[j]).bit_count()
        else:
            res += (not_friend[i] & not_friend[j]).bit_count()
print(res//3)
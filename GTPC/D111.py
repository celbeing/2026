n, m = map(int, input().split())
w = sorted(list(map(int, input().split())))

res = 0

for left in range(n):
    for right in range(left, n):
        if w[left] <= 0 <= w[right]:
            if min(abs(w[left])*2+w[right], abs(w[left])+w[right]*2) <= m:
                res = max(res, right-left+1)

print(res)
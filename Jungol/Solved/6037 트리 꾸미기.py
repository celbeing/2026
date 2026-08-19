n = int(input())
a = list(map(int, input().split()))
left = [-1] * (n+1)
right = [0] * (n+1)
total = 0
for i in range(n):
    if left[a[i]] == -1:
        left[a[i]] = i
        total += 1
    right[a[i]] = i

dp = [[-n] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1 if left[a[i]] == right[a[i]] == i else 0

for k in range(2, n+1):
    for l in range(n-k+1):
        r = l+k-1

        L = 1 if left[a[l]] == l and right[a[l]] <= r else 0
        R = 1 if left[a[r]] >= l and right[a[r]] == r else 0

        dp[l][r] = max(L-dp[l+1][r], R-dp[l][r-1])

p = (total + dp[0][-1])//2
b = (total - dp[0][-1])//2
print(f'{p}:{b}')
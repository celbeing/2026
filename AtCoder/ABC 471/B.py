n = int(input())
ans = dict()
high = 0
for _ in range(n):
    a = input().strip().lower()
    if a in ans: ans[a] += 1
    else: ans[a] = 1
    high = max(high, ans[a])
print(high)
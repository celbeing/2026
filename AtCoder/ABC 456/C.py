s = input().strip()
res = 1
count = 1
mod = 998244353

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count = 1
    else:
        count += 1
    res += count
    res %= mod

print(res)
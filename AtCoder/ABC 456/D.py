s = input().strip()
mod = 998244353

dp = [0] * 3
prefix = [0] * 3
ab = {'a':0,'b':1,'c':2}

for i in range(len(s)):
    t = ab[s[i]]
    dp[t] = prefix[(t+1)%3] + prefix[(t+2)%3] + 1
    dp[t] %= mod
    prefix[t] += dp[t]
    prefix[t] %= mod

print(sum(prefix)%mod)
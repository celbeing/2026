n, k = map(int, input().split())
a = list(map(int, input().split()))
bulb = [a[0]]
memo = [[201] * n for _ in range(n)]
for t in a:
    if t == bulb[-1]: continue
    else: bulb.append(t)
def switching(l, r):
    if l >= r: return 0
    if memo[l][r] < 201: return memo[l][r]

    for m in range(l, r):
        memo[l][r] = min(memo[l][r], switching(l,m)+switching(m+1,r) + (0 if bulb[l] == bulb[m+1] else 1))
    if bulb[l] == bulb[r]:
        memo[l][r] = min(memo[l][r], switching(l+1,r-1)+1)
    return memo[l][r]

print(switching(0,len(bulb)-1))
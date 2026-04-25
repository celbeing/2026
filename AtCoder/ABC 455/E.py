n = int(input())
s = input().strip()
a, b, c = 0, 0, 0
ab = dict()
bc = dict()
ac = dict()
abc = dict()
ab[0] = 1
bc[0] = 1
ac[0] = 1
abc[(0,0)] = 1
for i in range(n):
    if s[i] == 'A': a += 1
    elif s[i] == 'B': b += 1
    else: c += 1

    if a-b in ab: ab[a-b] += 1
    else: ab[a-b] = 1

    if b-c in bc: bc[b-c] += 1
    else: bc[b-c] = 1

    if a-c in ac: ac[a-c] += 1
    else: ac[a-c] = 1

    if (a-b,a-c) in abc: abc[(a-b,a-c)] += 1
    else: abc[(a-b,a-c)] = 1

res = n*(n+1)//2
for i in ab:
    j = ab[i]
    res -= (j*(j-1))//2
for i in bc:
    j = bc[i]
    res -= (j*(j-1))//2
for i in ac:
    j = ac[i]
    res -= (j*(j-1))//2
for i in abc:
    j = abc[i]
    res += j*(j-1)

print(res)
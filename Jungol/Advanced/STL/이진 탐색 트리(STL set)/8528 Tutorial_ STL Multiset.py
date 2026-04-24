# hash_set

import sys
input = sys.stdin.readline

ms = dict()
for _ in range(int(input())):
    q, n = input().split()
    n = int(n)
    if q == 'i':
        if n in ms:
            ms[n] += 1
        else:
            ms[n] = 1
    elif q == 'r':
        if n in ms:
            if ms[n] == 1:
                del ms[n]
            else:
                ms[n] -= 1
    else:
        if n in ms:
            del ms[n]

res = []
for k in sorted(list(ms)):
    for t in range(ms[k]):
        res.append(k)
print(*res)
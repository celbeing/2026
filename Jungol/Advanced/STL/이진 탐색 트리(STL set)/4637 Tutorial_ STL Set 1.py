# hash_set

import sys
input = sys.stdin.readline

s = dict()
idx = 1
for _ in range(int(input())):
    q, n = input().split()
    n = int(n)
    if q == 'i':
        if not(n in s):
            s[n] = idx
            idx += 1
    else:
        if n in s:
            del s[n]

x = int(input())
for a in s:
    if x == s[a]:
        print(s[a])
        break
else:
    print('OVER')
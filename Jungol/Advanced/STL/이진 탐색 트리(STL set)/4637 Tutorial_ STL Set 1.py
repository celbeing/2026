# hash_set

import sys
input = sys.stdin.readline

s = set()
for _ in range(int(input())):
    q, n = input().split()
    n = int(n)
    if q == 'i':
        s.add(n)
    else:
        s.discard(n)
print(*sorted(list(s)))
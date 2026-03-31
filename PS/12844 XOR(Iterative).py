# python3: TLE, pypy3: 1500ms

import sys

n = int(input())
a = list(map(int, input().split()))

size = 1
while size < n: size <<= 1

seg = [0] * size * 2
lazy = [0] * size * 2
leaf_count = [0] * size * 2
LOG = size.bit_length() - 1

for i in range(n):
    seg[size + i] = a[i]
    leaf_count[size + i] = 1
for i in range(size - 1, 0, -1):
    seg[i] = seg[i*2] ^ seg[i*2+1]
    leaf_count[i] = leaf_count[i*2] ^ leaf_count[i*2+1]

def apply(node, k):
    if leaf_count[node]:
        seg[node] ^= k
    if node < size:
        lazy[node] ^= k
    return

def push(node):
    for s in range(LOG, 0, -1):
        i = node >> s
        if lazy[i]:
            apply(i*2, lazy[i])
            apply(i*2+1, lazy[i])
            lazy[i] = 0
    return

def pull(node):
    while node > 1:
        node >>= 1
        seg[node] = seg[node*2] ^ seg[node*2+1]
        if leaf_count[node]:
            seg[node] ^= lazy[node]

def update(l, r, k):
    l += size
    r += size
    l0, r0 = l, r

    push(l0)
    push(r0)

    while l <= r:
        if l & 1:
            apply(l, k)
            l += 1
        if not(r & 1):
            apply(r, k)
            r -= 1
        l >>= 1
        r >>= 1

    pull(l0)
    pull(r0)
    return

def query(l, r):
    l += size
    r += size
    push(l)
    push(r)

    res = 0
    while l <= r:
        if l & 1:
            res ^= seg[l]
            l += 1
        if not(r & 1):
            res ^= seg[r]
            r -= 1
        l >>= 1
        r >>= 1
    return res

out = []
for _ in range(int(input())):
    line = list(map(int, input().split()))
    if line[0] == 1:
        update(line[1], line[2], line[3])
    else:
        out.append(query(line[1], line[2]))

sys.stdout.write('\n'.join(map(str, out)))
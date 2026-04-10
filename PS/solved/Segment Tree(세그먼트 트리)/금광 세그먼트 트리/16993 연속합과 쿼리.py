# Python3 : 2292ms, PyPy3 : 3188ms

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
void = -float('inf')

size = 1
while size < n:
    size <<= 1

seg = [0] * size * 2
l_max = [void] * size * 2
r_max = [void] * size * 2
t_max = [void] * size * 2

for i in range(n):
    seg[size+i] = arr[i]
    l_max[size+i] = arr[i]
    r_max[size+i] = arr[i]
    t_max[size+i] = arr[i]
for i in range(size-1, 0, -1):
    seg[i] = seg[i*2] + seg[i*2+1]
    l_max[i] = max(l_max[i*2], seg[i*2] + l_max[i*2+1])
    r_max[i] = max(r_max[i*2+1], seg[i*2+1] + r_max[i*2])
    t_max[i] = max(max(t_max[i*2], t_max[i*2+1]), r_max[i*2] + l_max[i*2+1])

for _ in range(int(input())):
    l, r = map(int, input().split())
    l += size-1; r += size-1
    l_merge = []
    r_merge = []
    while l < r:
        if l & 1:
            l_merge.append(l)
            l += 1
        l >>= 1
        if not(r & 1):
            r_merge.append(r)
            r -= 1
        r >>= 1
    if l == r:
        l_merge.append(l)
    r_merge.reverse()
    l_merge += r_merge

    right, total = r_max[l_merge[0]], t_max[l_merge[0]]
    for i in range(1, len(l_merge)):
        total = max(max(total, right+l_max[l_merge[i]]), t_max[l_merge[i]])
        right = max(right+seg[l_merge[i]], r_max[l_merge[i]])

    print(max(total, right))
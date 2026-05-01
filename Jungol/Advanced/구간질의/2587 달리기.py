import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
x_set = set()
x_set.update(a)
x_map = dict()
for i, x in enumerate(sorted(list(x_set))):
    x_map[x] = i

res = []
fw = [0] * (len(x_set)+1)
for k in a:
    k = len(x_set) - x_map[k]

    idx = k
    while idx <= len(x_set):
        fw[idx] += 1
        idx += idx&-idx
    idx = k - 1
    p = 0
    while idx:
        p += fw[idx]
        idx -= idx&-idx
    res.append(str(p+1))

print('\n'.join(res))
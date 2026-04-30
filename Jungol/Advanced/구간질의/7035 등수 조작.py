import sys
input = sys.stdin.readline

n, q= map(int, input().split())
fw = [0] * 100001
a = list(map(int, input().split()))
for k in a:
    fw[k] += 1
for i in range(1, 100001):
    j = i+(i&-i)
    if j <= 100000:
        fw[j] += fw[i]

def prefix_sum(idx):
    result = 0
    while idx:
        result += fw[idx]
        idx -= idx&-idx
    return result

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = a[query[1]-1]
        print(n-prefix_sum(x)+1)
    else:
        x, y = query[1:]
        idx = a[x-1]
        while idx <= 100000:
            fw[idx] -= 1
            idx += idx&-idx
        a[x-1] = y
        idx = y
        while idx <= 100000:
            fw[idx] += 1
            idx += idx&-idx

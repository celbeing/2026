import sys
input = sys.stdin.readline

n = int(input())
size = 1
while size < n:
    size <<= 1
seg = [[] for _ in range(size * 2)]
a = list(map(int, input().split()))

for i in range(n):
    seg[size+i].append(a[i])
for i in range(size-1, 0, -1):
    l, r = 0, 0
    while len(seg[i*2]) > l and len(seg[i*2+1]) > r:
        if seg[i*2][l] < seg[i*2+1][r]:
            seg[i].append(seg[i*2][l])
            l += 1
        else:
            seg[i].append(seg[i*2+1][r])
            r += 1

    while len(seg[i*2]) > l:
        seg[i].append(seg[i*2][l])
        l += 1
    while len(seg[i*2+1]) > r:
        seg[i].append(seg[i*2+1][r])
        r += 1

def bin_search(arr, k):
    s, e = 0, len(arr)
    while s < e:
        m = (s+e)//2
        if arr[m] < k:
            s = m + 1
        else:
            e = m
    return len(arr) - e

for _ in range(int(input())):
    i, j, k = map(int, input().split())
    i += size-1
    j += size-1
    node = []
    while i < j:
        if i & 1:
            node.append(i)
            i += 1
        i >>= 1
        if not(j & 1):
            node.append(j)
            j -= 1
        j >>= 1
    if i == j:
        node.append(i)

    result = 0
    for nd in node:
        result += bin_search(seg[nd], k+1)

    print(result)
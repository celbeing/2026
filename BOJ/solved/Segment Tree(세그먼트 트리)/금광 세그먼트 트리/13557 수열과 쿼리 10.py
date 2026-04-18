import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

size = 1
while size < n:
    size <<= 1

INF = -float('inf')
seg = [0] * size * 2
l_seg = [INF] * size * 2
r_seg = [INF] * size * 2
t_seg = [INF] * size * 2

for i in range(n):
    seg[size+i] = a[i]
    l_seg[size+i] = a[i]
    r_seg[size+i] = a[i]
    t_seg[size+i] = a[i]
for i in range(size-1,0,-1):
    seg[i] = seg[i*2]+seg[i*2+1]
    l_seg[i] = max(l_seg[i*2], seg[i*2]+l_seg[i*2+1])
    r_seg[i] = max(r_seg[i*2+1], seg[i*2+1]+r_seg[i*2])
    t_seg[i] = max(t_seg[i*2],t_seg[i*2+1],r_seg[i*2]+l_seg[i*2+1])

def l_query(i, j):
    if i > j: return 0
    node, merge = [], []
    while i < j:
        if i & 1:
            merge.append(i)
            i += 1
        i >>= 1
        if not (j & 1):
            node.append(j)
            j -= 1
        j >>= 1
    if i == j:
        node.append(j)
    node += reversed(merge)
    left = INF
    sum = 0
    for k in node:
        left = max(left, sum + r_seg[k])
        sum += seg[k]
    return left

def r_query(i, j):
    if i > j: return 0
    node, merge = [], []
    while i < j:
        if i & 1:
            node.append(i)
            i += 1
        i >>= 1
        if not (j & 1):
            merge.append(j)
            j -= 1
        j >>= 1
    if i == j:
        node.append(i)
    node += reversed(merge)
    right = INF
    sum = 0
    for k in node:
        right = max(right, sum + l_seg[k])
        sum += seg[k]
    return right

def t_query(i, j):
    if i > j: return 0
    node, merge = [], []
    while i < j:
        if i & 1:
            node.append(i)
            i += 1
        i >>= 1
        if not (j & 1):
            merge.append(j)
            j -= 1
        j >>= 1
    if i == j:
        node.append(j)
    node += reversed(merge)
    total = INF
    right = INF
    for k in node:
        total = max(total, t_seg[k], right + l_seg[k])
        right = max(r_seg[k], right + seg[k])
    return total

def s_query(i, j):
    sum = 0
    while i < j:
        if i & 1:
            sum += seg[i]
            i += 1
        i >>= 1
        if not(j & 1):
            sum += seg[j]
            j -= 1
        j >>= 1
    if i == j:
        sum += seg[i]
    return sum

for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    a,b,c,d = a+size-1,b+size-1,c+size-1,d+size-1
    res = 0

    if b < c:
        p, q, r = l_query(a, b), s_query(b+1, c-1), r_query(c, d)
        print(p+q+r)
    else:
        p = l_query(a, c-1)
        q = r_query(c, b)
        r = t_query(c, b)
        s = l_query(c, b)
        t = r_query(b+1, d)
        u = s_query(c, b)
        print(max(p+q, r, s+t,p+u+t))
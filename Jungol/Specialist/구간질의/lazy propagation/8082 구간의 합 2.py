n = int(input())
size = 1
while size < n:
    size <<= 1

seg = [0] * size * 2
cnt = [0] * size * 2
lazy = [0] * size * 2

a = list(map(int, input().split()))
for i in range(n):
    seg[i+size] = a[i]
    cnt[i+size] = 1
for i in range(size-1,0,-1):
    seg[i] = seg[i*2] + seg[i*2+1]
    cnt[i] = cnt[i*2] + cnt[i*2+1]

def apply(node, x):
    seg[node] += cnt[node] * x
    lazy[node] += x

def push(node):
    if lazy[node]:
        if node < size:
            apply(node*2, lazy[node])
            apply(node*2+1, lazy[node])
        lazy[node] = 0

def push_path(node):
    path = []
    node >>= 1
    while node:
        path.append(node)
        node >>= 1
    for x in reversed(path):
        push(x)

def build_path(node):
    node >>= 1
    while node:
        seg[node] = seg[node*2] + seg[node*2+1] + lazy[node]*cnt[node]
        node >>= 1

for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        l, r, x = q[1:]
        l, r = l+size-1, r+size-1
        push_path(l)
        push_path(r)

        while l < r:
            if l & 1:
                apply(l, x)
                l += 1
            l >>= 1
            if not(r & 1):
                apply(r, x)
                r -= 1
            r >>= 1

        if l == r:
            apply(l, x)

        l, r = q[1]+size-1, q[2]+size-1
        build_path(l)
        build_path(r)

    else:
        l, r = q[1:]
        l, r = l+size-1, r+size-1

        push_path(l)
        push_path(r)

        res = 0

        while l < r:
            if l & 1:
                res += seg[l]
                l += 1
            l >>= 1
            if not(r & 1):
                res += seg[r]
                r -= 1
            r >>= 1
        if l == r:
            res += seg[l]

        print(res)
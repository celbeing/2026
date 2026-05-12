n, m = map(int, input().split())
size = 1
while size < n:
    size <<= 1

seg = [0] * size * 2
cnt = [0] * size * 2
lazy = [0] * size * 2
for i in range(n):
    cnt[size+i] = 1
for i in range(size-1,0,-1):
    cnt[i] = cnt[i*2]+cnt[i*2+1]

def apply(node):
    seg[node] = cnt[node]-seg[node]
    lazy[node] ^= 1

def push(node):
    if lazy[node]:
        if node < size:
            apply(node*2)
            apply(node*2+1)
        lazy[node] = 0

def push_path(node):
    stack = []
    node >>= 1
    while node:
        stack.append(node)
        node >>= 1
    for x in reversed(stack):
        push(x)

def build_path(node):
    node >>= 1
    while node:
        seg[node] = seg[node*2]+seg[node*2+1]
        if lazy[node]:
            seg[node] = cnt[node] - seg[node]
        node >>= 1

for _ in range(m):
    q, s, e= map(int, input().split())
    l, r = s + size - 1, e + size - 1
    push_path(l)
    push_path(r)

    if q:
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
    else:
        while l < r:
            if l & 1:
                apply(l)
                l += 1
            l >>= 1
            if not(r & 1):
                apply(r)
                r -= 1
            r >>= 1
        if l == r:
            apply(l)

        l, r = s+size-1, e+size-1
        build_path(l)
        build_path(r)
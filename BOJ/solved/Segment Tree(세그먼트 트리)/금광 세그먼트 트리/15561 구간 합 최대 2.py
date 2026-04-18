import sys
input = sys.stdin.readline

n, q, u, v = map(int, input().split())
k = list(map(int, input().split()))
INF = int(1e9)

size = 1
while size < n:
    size <<= 1

prefix_seg = [0] * size * 2
struct_seg = [-INF] * size * 2
struct_left = [-INF] * size * 2
struct_right = [-INF] * size * 2
for i in range(n):
    prefix_seg[size+i] = k[i] * u + v
    struct_seg[size+i] = k[i] * u + v
    struct_left[size+i] = k[i] * u + v
    struct_right[size+i] = k[i] * u + v
for i in range(size-1,0,-1):
    prefix_seg[i] = prefix_seg[i*2] + prefix_seg[i*2+1]
    struct_left[i] = max(struct_left[i*2], prefix_seg[i*2]+struct_left[i*2+1])
    struct_right[i] = max(struct_right[i*2+1], prefix_seg[i*2+1]+struct_right[i*2])
    struct_seg[i] = max(max(struct_seg[i*2], struct_seg[i*2+1]), struct_right[i*2]+struct_left[i*2+1])

for _ in range(q):
    c, a, b = map(int, input().split())
    if c:
        a += size-1
        prefix_seg[a] = b * u + v
        struct_seg[a] = b * u + v
        struct_left[a] = b * u + v
        struct_right[a] = b * u + v
        a >>= 1
        while a:
            prefix_seg[a] = prefix_seg[a*2] + prefix_seg[a*2+1]
            struct_left[a] = max(struct_left[a*2], prefix_seg[a*2] + struct_left[a*2+1])
            struct_right[a] = max(struct_right[a*2+1], prefix_seg[a*2+1] + struct_right[a*2])
            struct_seg[a] = max(max(struct_seg[a*2], struct_seg[a*2+1]), struct_right[a*2] + struct_left[a*2+1])
            a >>= 1
    else:
        a, b = a+size-1, b+size-1
        node = []
        right_node = []
        while a < b:
            if a & 1:
                node.append(a)
                a += 1
            a >>= 1

            if not(b & 1):
                right_node.append(b)
                b -= 1
            b >>= 1

        if a == b:
            node.append(a)

        node += reversed(right_node)

        total = -INF
        right = -INF

        for i in node:
            total = max(max(total, struct_seg[i]), right + struct_left[i])
            right = max(right + prefix_seg[i], struct_right[i])

        print(total - v)
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
pos = dict()

size = 1
while size < n:
    size <<= 1

min_seg = [n+1] * size * 2
max_seg = [0] * size * 2

stu = list(map(int, input().split()))
for i in range(n):
    min_seg[size+stu[i]-1] = i
    max_seg[size+stu[i]-1] = i
    pos[i+1] = stu[i]
for i in range(size-1,0,-1):
    min_seg[i] = min(min_seg[i*2], min_seg[i*2+1])
    max_seg[i] = max(max_seg[i*2], max_seg[i*2+1])

for _ in range(m):
    q, x, y = map(int, input().split())
    if q == 1:
        a, b = pos[x], pos[y]
        pos[x], pos[y] = pos[y], pos[x]
        x, y = a+size-1, b+size-1
        min_seg[x], min_seg[y] = min_seg[y], min_seg[x]
        max_seg[x], max_seg[y] = max_seg[y], max_seg[x]
        x >>= 1
        y >>= 1
        while x:
            min_seg[x] = min(min_seg[x*2], min_seg[x*2+1])
            min_seg[y] = min(min_seg[y*2], min_seg[y*2+1])
            max_seg[x] = max(max_seg[x*2], max_seg[x*2+1])
            max_seg[y] = max(max_seg[y*2], max_seg[y*2+1])
            x >>= 1
            y >>= 1
    else:
        gap = y - x
        x, y = x+size-1, y+size-1
        min_num, max_num = n+1, 0
        while x < y:
            if x & 1:
                min_num = min(min_num, min_seg[x])
                max_num = max(max_num, max_seg[x])
                x += 1
            x >>= 1
            if not(y & 1):
                min_num = min(min_num, min_seg[y])
                max_num = max(max_num, max_seg[y])
                y -= 1
            y >>= 1
        if x == y:
            min_num = min(min_num, min_seg[x])
            max_num = max(max_num, max_seg[x])

        print('YES' if max_num-min_num == gap else 'NO')
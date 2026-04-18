import sys
input = sys.stdin.readline

n = int(input())
mine = []

# 좌표 압축
x_set = set()
y_set = set()
for _ in range(n):
    x, y, w = map(int, input().split())
    mine.append((x, y, w))
    x_set.add(x)
    y_set.add(y)
x_map = dict()
y_map = dict()
for x1_point, x in enumerate(sorted(x_set)):
    x_map[x] = x1_point
for y1_point, y in enumerate(sorted(y_set)):
    y_map[y] = y1_point

y_point = [[] for _ in range(y1_point+1)]
for x, y, w in mine:
    y_point[y_map[y]].append((x_map[x], w))

size = 1
n = len(x_set)
while size < n:
    size <<= 1

result = 0
INF = -float('inf')
for i in range(y1_point+1):
    seg = [0] * size * 2
    left_seg = [0] * size * 2
    right_seg = [0] * size * 2
    total_seg = [0] * size * 2

    for x, w in y_point[i]:
        seg[size+x] += w
        left_seg[size+x] = w
        right_seg[size+x] = w
        total_seg[size+x] = w
    for j in range(size-1,0,-1):
        seg[j] = seg[j*2] + seg[j*2+1]
        left_seg[j] = max(left_seg[j*2], seg[j*2] + left_seg[j*2+1])
        right_seg[j] = max(right_seg[j*2+1], right_seg[j*2] + seg[j*2+1])
        total_seg[j] = max(total_seg[j*2], total_seg[j*2+1], right_seg[j*2] + left_seg[j*2+1])
    result = max(result, total_seg[1])
    for j in range(i+1,y1_point+1):
        for x, w in y_point[j]:
            seg[size+x] += w
            left_seg[size+x] += w
            right_seg[size+x] += w
            total_seg[size+x] += w
            idx = (size+x) >> 1
            while idx:
                seg[idx] = seg[idx*2] + seg[idx*2+1]
                left_seg[idx] = max(left_seg[idx*2], seg[idx*2] + left_seg[idx*2+1])
                right_seg[idx] = max(right_seg[idx*2+1], right_seg[idx*2] + seg[idx*2+1])
                total_seg[idx] = max(total_seg[idx*2], total_seg[idx*2+1], right_seg[idx*2] + left_seg[idx*2+1])
                idx >>= 1
        result = max(result, total_seg[1])

print(result)
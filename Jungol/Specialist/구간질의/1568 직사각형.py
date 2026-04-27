import sys
input = sys.stdin.readline

n = int(input())
y_set = set()
lines = []
y_interval = []
for _ in range(n):
    x1, x2, y1, y2 = map(int, input().split())
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1

    y_set.add(y1)
    y_set.add(y2)

    lines.append((x1,1,y1,y2))
    lines.append((x2,-1,y1,y2))
lines.sort()

y_val = dict()
y_key = dict()

for i, y in enumerate(sorted(list(y_set))):
    y_val[i] = y
    y_key[y] = i
    if i > 0:
        y_interval.append(y-y_val[i-1])

y_cnt = len(y_val)
size = 1
while size < y_cnt:
    size <<= 1
cover_seg = [0] * size * 2
count_seg = [0] * size * 2
total_seg = [0] * size * 2

for i in range(y_cnt-1):
    total_seg[i+size] = y_interval[i]
for i in range(size-1,0,-1):
    total_seg[i] = total_seg[i*2]+total_seg[i*2+1]

def cover_update(l, r, w):
    l, r = y_key[l]+size, y_key[r]-1+size
    while l < r:
        if l & 1:
            cover_seg[l] += w
            if cover_seg[l] == 0: delete_sq(l)
            else: create_dq(l)
            l += 1
        l >>= 1

        if not(r & 1):
            cover_seg[r] += w
            if cover_seg[r] == 0: delete_sq(r)
            else: create_dq(r)
            r -= 1
        r >>= 1

    if l == r:
        cover_seg[l] += w
        if cover_seg[l] == 0: delete_sq(l)
        else: create_dq(l)

def delete_sq(node):
    if node >= size:
        count_seg[node] = 0
        node >>= 1
    while node:
        count_seg[node] = count_seg[node*2]+count_seg[node*2+1]
        node >>= 1

def create_dq(node):
    count_seg[node] = total_seg[node]
    node >>= 1
    while node:
        count_seg[node] = count_seg[node*2]+count_seg[node*2+1]
        node >>= 1

last = 0
result = 0
# lines에서 선분 하나씩 불러오고 counter에 갱신
for x, w, y1, y2 in lines:
    result += count_seg[1] * (x-last)
    cover_update(y1,y2,w)
    last = x

print(result)
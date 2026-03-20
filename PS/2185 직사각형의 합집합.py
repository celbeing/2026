import sys
input = sys.stdin.readline

n = int(input())
lines_x = []
lines_y = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    x1 += 10000
    x2 += 10000
    y1 += 10000
    y2 += 10000
    lines_x.append((x1, -1, y1, y2-1))
    lines_x.append((x2, 1, y1, y2-1))
    lines_y.append((y1, -1, x1, x2-1))
    lines_y.append((y2, 1, x1, x2-1))
lines_x.sort()
lines_y.sort()

result = 0

last = 0
seg = [0] * 20001 * 8
cnt = [0] * 20001 * 8

def update_tree(node, start, end, left, right, w):
    if end < left or right < start: return

    if left <= start and end <= right:
        cnt[node] -= w
    else:
        mid = (start + end) // 2
        update_tree(node * 2, start, mid, left, right, w)
        update_tree(node * 2 + 1, mid + 1, end, left, right, w)

    if cnt[node] > 0:
        seg[node] = end - start + 1
    else:
        seg[node] = seg[node * 2] + seg[node * 2 + 1]

for x, w, b, t in lines_x:
    update_tree(1, 0, 20000, b, t, w)
    result += abs(last - seg[1])
    last = seg[1]

last = 0
seg = [0] * 20001 * 8
cnt = [0] * 20001 * 8

for y, w, l, r in lines_y:
    update_tree(1, 0 , 20000, l, r, w)
    result += abs(last - seg[1])
    last = seg[1]

print(result)
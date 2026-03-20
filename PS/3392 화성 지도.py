import sys
input = sys.stdin.readline

cnt = [0] * 30002 * 8   # 덮고 있는 사각형의 수
seg = [0] * 30002 * 8   # 비어있지 않은 곳의 수

def update_tree(node, start, end, left, right, w):
    # update 범위를 벗어난 경우
    if end < left or start > right: return

    # 탐색 범위가 update 범위에 모두 포함되는 경우
    if left <= start and end <= right:
        cnt[node] += w
    # 탐색 범위가 update 범위에 걸친 경우
    else:
        mid = (start + end) // 2
        update_tree(node * 2, start, mid, left, right, w)
        update_tree(node * 2 + 1, mid + 1, end, left, right, w)

    # 탐색 범위 전체가 다 덮인 경우
    # seg의 현재 위치 갱신
    if cnt[node] > 0:
        seg[node] = end - start + 1
    else:
        seg[node] = seg[node * 2] + seg[node * 2 + 1]

n = int(input())
lines = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append((x1, y1, y2-1, 1))
    lines.append((x2, y1, y2-1, -1))
lines.sort()

last = 0
result = 0
for x, b, t, w in lines:
    l = x - last
    last = x
    result += l * seg[1]

    update_tree(1, 0, 30000, b, t, w)

print(result)
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

for y1_point, x in enumerate(sorted(x_set)):
    x_map[x] = y1_point

for y1_point, y in enumerate(sorted(y_set)):
    y_map[y] = y1_point

for y1_point in range(n):
    mine[y1_point] = (y_map[mine[y1_point][1]], x_map[mine[y1_point][0]], mine[y1_point][2])

mine.sort()


# seg의 size 결정
size = 1
n = len(x_set)
while size < n:
    size <<= 1

last_start = -1

result = 0
y1_point = 0
while y1_point < len(y_set):
    # y1_point가 가리키는 y에 대해 seg 초기화
    seg = [0] * size * 2
    while y1_point < len(y_set) and mine[y1_point][0] >= last_start:
        last_start = mine[y1_point][0]
        node = size + mine[y1_point][1]
        while node:
            seg[node] += mine[y1_point][2]
            node >>= 1
        y1_point += 1

    # y2_point에 대해 seg 트리 갱신
    last_end = mine[y2_point][0]
    y2_point = y1_point
    while y2_point < len(y_set) and mine[y2_point][0] >= last_end:
        last_end = mine[y2_point][0]
        node = size + mine[y2_point][1]
        while node:
            seg[node] += mine[y2_point][2]
            node >>= 1
        y2_point += 1

    # 구간 최대합 구하기

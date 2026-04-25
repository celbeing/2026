import sys
input = sys.stdin.readline

n = int(input())
y_set = set()
lines = []
for _ in range(n):
    x1, x2, y1, y2 = map(int, input().split())
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1

    y_set.add(y1)
    y_set.add(y2-1)

    lines.append((x1,1,y1,y2-1))
    lines.append((x2,-1,y1,y2-1))
lines.sort()

y_val = dict()
y_key = dict()
for i, y in enumerate(sorted(list(y_set))):
    y_val[i] = y
    y_key[y] = i

y_cnt = len(y_val)
size = 1
while size < y_cnt:
    size <<= 1
covered = [0] * size * 2
counter = [0] * size * 2

# lines에서 선분 하나씩 불러오고 counter에 갱신
# lazy propagation
#
# 그리고 0이 아닌 구간 길이를 covered tree에서 확인
# delta x에 대해 covered[1]을 곱해서 스위핑
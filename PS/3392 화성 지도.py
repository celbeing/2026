import sys
input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append((x1, y1, y2, 1))
    lines.append((x2, y1, y2, -1))

y_count = [0] * 30_001
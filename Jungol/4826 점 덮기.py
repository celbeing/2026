n = int(input())
dots = []
for _ in range(n):
    x, y = map(int, input().split())
    dots.append((abs(x), abs(y)))
dots.sort(key = lambda x:(-x[1], -x[0]))
area = 0
w, h = 0, 50000000
# 모서리 되는 지점 먼저 추출
# 높은 순서대로 확인하면서 dp
# dp[i][j] = i번째 점을 j개의 사각형으로 처리하는 최적해
for x, y in dots:
    if x <= w: continue
    a1 = x*y
    a2 = h*(x-w)
    if a1 < a2:
        area += a1
        w, h = x, y
    else:
        area += a2
        w = x
print(area*4)
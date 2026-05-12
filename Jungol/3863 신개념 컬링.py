import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def ccw(p0, p1, p2):
    k = (p1[1]-p0[1])*(p2[0]-p1[0])-(p1[0]-p0[0])*(p2[1]-p1[1])
    if k > 0: return 1
    elif k < 0: return -1
    else: return 0

def graham(dots):
    upper, lower = [], []
    for p in dots:
        while len(upper) > 1 and ccw(upper[-2],upper[-1],p) <= 0:
            upper.pop()
        upper.append(p)
    for p in reversed(dots):
        while len(lower) > 1 and ccw(lower[-2],lower[-1],p) <= 0:
            lower.pop()
        lower.append(p)
    lower.reverse()
    return upper, lower

n = int(input())
our = sorted([tuple(map(int, input().split())) for _ in range(n)])
opo = sorted([tuple(map(int, input().split())) for _ in range(n)])
our_upper, our_lower = graham(our)
opo_upper, opo_lower = graham(opo)

# 각 점을 순서대로 살펴보며 upper, lower에 대해 투 포인터 탐색 실시
# 포인터가 가리키는 점들로 만들어진 선분이 확인하고 있는 점의 x좌표에 대해
# y값이 얼마인지 찾고 확인하고 있는 점의 y좌표가 lower<=y<=upper인가 확인
# edgecase: 시작 또는 끝 선분에 걸치는 경우, 기울기가 없기 때문에
# upper의 경우 뒤쪽 포인터의 y좌표, lower의 경우 앞쪽 포인터의 y좌표로 확인한다.
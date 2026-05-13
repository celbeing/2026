import sys
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

our_point, opo_point = 0, 0
l1,l2,u1,u2 = 0,1,0,1

# 상대팀 선분으로 우리팀 점수 확인
for x, y in our:
    # 점의 x좌표가 볼록껍질보다 왼쪽일 때
    if x < opo_upper[u1][0]: continue

    # 위쪽 껍질이 너무 앞에 있을 때
    while u2 < len(opo_upper) and opo_upper[u2][0] < x:
        u1 += 1; u2 += 1
    # 위쪽 껍질이 이미 끝났을 때
    if u2 == len(opo_upper): break

    # 아래쪽 껍질이 너무 앞에 있을 때
    while l2 < len(opo_lower) and opo_lower[l2][0] < x:
        l1 += 1; l2 += 1
    # 아래쪽 껍질이 이미 끝났을 때
    if l2 == len(opo_lower): break

    # y축에 평행한 껍질에 걸친 경우
    if opo_upper[u1][0] == opo_upper[u2][0]:
        if opo_upper[u1][1] <= y <= opo_upper[u2][1]:
            opo_point += 1
        continue
    if opo_lower[l1][0] == opo_lower[l2][0]:
        if opo_lower[l1][1] <= y <= opo_lower[l2][1]:
            opo_point += 1
        continue

    upper_y = opo_upper[u1][1] + (opo_upper[u1][1]-opo_upper[u2][1])/(opo_upper[u1][0]-opo_upper[u2][0])*(x-opo_upper[u1][0])
    lower_y = opo_lower[l1][1] + (opo_lower[l1][1]-opo_lower[l2][1])/(opo_lower[l1][0]-opo_lower[l2][0])*(x-opo_lower[l1][0])
    if lower_y <= y <= upper_y:
        opo_point += 1

l1,l2,u1,u2 = 0,1,0,1
for x, y in opo:
    if x < our_upper[u1][0]: continue

    while u2 < len(our_upper) and our_upper[u2][0] < x:
        u1 += 1; u2 += 1
    if u2 == len(our_upper): break

    while l2 < len(our_lower) and our_lower[l2][0] < x:
        l1 += 1; l2 += 1
    if l2 == len(our_lower): break

    if our_upper[u1][0] == our_upper[u2][0]:
        if our_upper[u1][1] <= y <= our_upper[u2][1]:
            our_point += 1
        continue
    if our_lower[l1][0] == our_lower[l2][0]:
        if our_lower[l1][1] <= y <= our_lower[l2][1]:
            our_point += 1
        continue

    upper_y = our_upper[u1][1] + (our_upper[u1][1]-our_upper[u2][1])/(our_upper[u1][0]-our_upper[u2][0])*(x-our_upper[u1][0])
    lower_y = our_lower[l1][1] + (our_lower[l1][1]-our_lower[l2][1])/(our_lower[l1][0]-our_lower[l2][0])*(x-our_lower[l1][0])
    if lower_y <= y <= upper_y:
        our_point += 1

print(our_point, opo_point)
# 각 점을 순서대로 살펴보며 upper, lower에 대해 투 포인터 탐색 실시
# 포인터가 가리키는 점들로 만들어진 선분이 확인하고 있는 점의 x좌표에 대해
# y값이 얼마인지 찾고 확인하고 있는 점의 y좌표가 lower<=y<=upper인가 확인
# edgecase: 시작 또는 끝 선분에 걸치는 경우, 기울기가 없기 때문에
# upper의 경우 뒤쪽 포인터의 y좌표, lower의 경우 앞쪽 포인터의 y좌표로 확인한다.
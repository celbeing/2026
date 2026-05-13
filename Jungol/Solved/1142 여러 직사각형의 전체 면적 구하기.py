import sys
input = sys.stdin.readline
n = int(input())
lines = []
for _ in range(n):
    x1, y1, w, h = map(float, input().split())
    x1 *= 10; y1 *= 10; w *= 10; h *= 10
    x1, y1, w, h = map(int, (x1, y1, w, h))
    lines.append((x1, y1, h, 1))
    lines.append((x1+w, y1, h, -1))

lines.sort()

result = 0
last = 0
point = dict()
for x, b, l, w in lines:
    count = 0
    length = 0
    reach = 0
    current_point = []
    for p, q in point: current_point.append((p, q))
    current_point.sort()
    if current_point:
        length += current_point[0][1]
        reach = current_point[0][0]+current_point[0][1]
        for p, q in current_point[1:]:
            if p+q <= reach: continue

            if p >= reach:
                length += q
                reach = p+q
            else:
                length += p+q-reach
                reach = p+q
    result += (x-last)*length
    last = x
    if (b,l) in point:
        point[(b,l)] += w
        if point[(b, l)] == 0:
            point.pop((b, l))
    else:
        point[(b,l)] = 1
if result % 100 == 0:
    print(result//100)
else:
    print(f"{result/100:.2f}")
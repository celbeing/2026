from collections import deque
n, k = map(int, input().split())

lim = 100000000
check = set()
check.add(n)
dq = deque([(n, 0, [n])])
count = 0
while True:
    now, depth, route = dq.popleft()
    count += 1
    if now == k:
        print(depth)
        print(*route)
        print(count)
        break

    nxt = [now * 3 + 1, now * 5 - 1, now // 2]
    for next in nxt:
        if not next in check and 0 < next <= lim:
            check.add(next)
            dq.append((next, depth + 1, route + [next]))
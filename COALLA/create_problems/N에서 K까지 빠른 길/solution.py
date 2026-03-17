from random import randint
from collections import deque

def solution(n, k):
    lim = 10_000_000
    check = set()
    check.add(k)
    check.add(0)
    dq = deque([(k, 0)])

    count = 0

    while dq:
        now, depth = dq.popleft()
        count += 1
        if now == n:
            return depth, count

        if (now - 1) % 3 == 0:
            nxt = (now - 1) // 3
            if not nxt in check:
                check.add(nxt)
                dq.append((nxt, depth + 1))

        if (now + 1) % 5 == 0:
            nxt = (now + 1) // 5
            if not nxt in check:
                check.add(nxt)
                dq.append((nxt, depth + 1))

        nxt = now * 2
        if nxt <= lim and not nxt in check:
            check.add(nxt)
            dq.append((nxt, depth + 1))

        if nxt < lim and not nxt + 1 in check:
            check.add(nxt + 1)
            dq.append((nxt + 1, depth + 1))

    return -1, -1

while True:
    n, k = randint(1, 10_000_000), randint(1, 10_000_000)
    print(n, k, solution(n, k))
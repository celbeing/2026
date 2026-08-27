import io
input = io.BufferedReader(io.FileIO(0), 1 << 18).readline
from collections import deque

def solution():
    while True:
        n, a, b = map(int, input().split())
        if n == a == b == 0: break

        team = []
        for _ in range(n):
            k, da, db = map(int, input().split())
            team.append((da-db, k, da, db))
        dq = deque(sorted(team))

        res = 0
        while dq:
            if dq[0][0] <= -dq[-1][0]:
                p, k, da, db = dq.popleft()
                if a >= k:
                    res += da * k
                    a -= k
                else:
                    res += da * a
                    k -= a
                    a = 0
                    res += db * k
            else:
                p, k, da, db = dq.pop()
                if b >= k:
                    res += db * k
                    b -= k
                else:
                    res += db * b
                    k -= b
                    b = 0
                    res += da * k
        print(res)
solution()
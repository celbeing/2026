import sys
from collections import deque
input = sys.stdin.readline

def solution():
    def shot(state, t):
        ret = 0
        k = 1
        for i in range(n):
            if i != t and state & k:
                ret |= tree[i]
            k <<= 1
        return ret

    while True:
        n, m = map(int, input().split())
        if n == m == 0: break
        tree = [0] * n
        depth = [-1] * (1<<n)
        route = [-1] * (1<<n)
        x_route = [-1] * (1<<n)
        depth[-1] = 0
        for _ in range(m):
            a, b = map(int, input().split())
            tree[a] |= 1 << b
            tree[b] |= 1 << a

        bfs = deque([(1<<n)-1])
        while bfs:
            now = bfs.popleft()
            if now == 0: break

            k = 1
            for i in range(n):
                next = shot(now, i)
                if depth[next] == -1:
                    depth[next] = depth[now]+1
                    route[next] = now
                    x_route[next] = i
                    bfs.append(next)
                k <<= 1

        if depth[0] > 0:
            res = []
            now = 0
            while route[now] > 0:
                res.append(x_route[now])
                next = route[now]
                now = next
            res.reverse()
            print(f'{depth[0]}:', *res)
        else:
            print('Impossible')

        input()

solution()

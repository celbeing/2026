import sys
from bisect import bisect_left


def solve():
    input = sys.stdin.buffer.readline
    n, l, m, k = map(int, input().split())
    inf = 10**30
    dist = [[inf] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dist[i][i] = 0
    for _ in range(l):
        u, v, t = map(int, input().split())
        if t < dist[u][v]:
            dist[u][v] = dist[v][u] = t
    for via in range(n + 1):
        row = dist[via]
        for u in range(n + 1):
            base = dist[u][via]
            for v in range(n + 1):
                candidate = base + row[v]
                if candidate < dist[u][v]:
                    dist[u][v] = candidate

    windows = [[] for _ in range(n)]
    for _ in range(m):
        i, a, b = map(int, input().split())
        windows[i - 1].append((a, b))
    starts, ends = [], []
    for intervals in windows:
        merged = []
        for a, b in sorted(intervals):
            if merged and a <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], b)
            else:
                merged.append([a, b])
        starts.append([a for a, _ in merged])
        ends.append([b for _, b in merged])

    # dp[mask * n + i]: earliest time after observing the selected
    # animals, with i being the last selected animal.
    # Incidental sightings on a route need not be recorded in this state.
    full = (1 << n) - 1
    unreachable = k + 1
    dp = [unreachable] * ((1 << n) * n)
    home = [dist[i + 1][0] for i in range(n)]
    for j in range(n):
        p = bisect_left(ends[j], dist[0][j + 1])
        if p < len(ends[j]):
            seen = max(dist[0][j + 1], starts[j][p])
            if seen + home[j] <= k:
                dp[(1 << j) * n + j] = seen

    answer = 0
    for mask in range(1, full + 1):
        offset = mask * n
        remaining = full ^ mask
        selected = mask
        while selected:
            bit = selected & -selected
            selected -= bit
            i = bit.bit_length() - 1
            current = dp[offset + i]
            if current == unreachable:
                continue
            answer = max(answer, mask.bit_count())
            if answer == n:
                print(n)
                return
            todo = remaining
            row = dist[i + 1]
            while todo:
                next_bit = todo & -todo
                todo -= next_bit
                j = next_bit.bit_length() - 1
                arrival = current + row[j + 1]
                if arrival + home[j] > k:
                    continue
                p = bisect_left(ends[j], arrival)
                if p == len(ends[j]):
                    continue
                seen = max(arrival, starts[j][p])
                if seen + home[j] <= k:
                    index = (mask | next_bit) * n + j
                    if seen < dp[index]:
                        dp[index] = seen
    print(answer)


if __name__ == '__main__':
    solve()

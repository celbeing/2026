from heapq import heappush, heappop

def solution():
    INF = float('inf')
    n, m, x = map(int, input().split())
    t = [0]+[int(input())-1 for _ in range(n)]
    graph = [[] for _ in range(n+1)]
    co = [(0,0,0)]
    for i in range(1, m+1):
        a, b, d = map(int, input().split())
        co.append((a, b, d))
        graph[a].append(i)
        graph[b].append(i)
    dist = [[[INF] * (x+1) for _ in range(3)] for _ in range(n+1)]
    dist[1][-1][0] = 0

    hq = [(0, 1, -1, 0)]
    while hq:
        d, now, state, past = heappop(hq)
        if dist[now][state][past] < d: continue

        for i in graph[now]:
            a, b, w = co[i]
            next = b if a == now else a
            next_state = t[next]
            nd = d+w
            next_past = min(past+w, x)
            if next_state == 0 and nd < dist[next][state][next_past]:
                dist[next][state][next_past] = nd
                heappush(hq, (nd, next, state, next_past))
            elif next_state == 1 and (state == 1 or next_past == x) and nd < dist[next][next_state][0]:
                dist[next][next_state][0] = nd
                heappush(hq, (nd, next, next_state, 0))
            elif next_state == -1 and (state == -1 or next_past == x) and nd < dist[next][next_state][0]:
                dist[next][next_state][0] = nd
                heappush(hq, (nd, next, next_state, 0))

    result = INF
    for state in (-1, 1):
        result = min(result, min(dist[n][state]))
    print(result)
solution()
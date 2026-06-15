import sys
input = sys.stdin.readline

def solution():
    for _ in range(int(input())):
        INF = int(1e9)
        n, m, b = map(int, input().split())
        graph = [dict() for _ in range(n+1)]
        for _ in range(m):
            u, v, w = map(int, input().split())
            if v in graph[u]:
                graph[u][v] = min(graph[v][u], w)
            else:
                graph[u][v] = w
            graph[v][u] = graph[u][v]
        for _ in range(b):
            s, e, t = map(int, input().split())
            if e in graph[s]:
                graph[s][e] = min(graph[s][e], -t)
            else:
                graph[s][e] = -t

        dist = [INF] * (n+1)
        dist[1] = 0
        for _ in range(n-1):
            for i in range(1, n+1):
                for j in graph[i]:
                    if dist[j] > dist[i]+graph[i][ j]:
                        dist[j] = dist[i]+graph[i][j]

        flag = False
        for i in range(1, n+1):
            for j in graph[i]:
                if dist[j] > dist[i] + graph[i][j]:
                    flag = True
                    break
            if flag: break

        print('YES' if flag else 'NO')
solution()
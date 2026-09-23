import sys
input = sys.stdin.readline

def solution():
    n, m, k = map(int, input().split())
    graph = [set() for _ in range(n+1)]
    link = []
    for _ in range(m):
        a, b = map(int, input().split())
        link.append((a, b))
        graph[a].add(b)
        graph[b].add(a)

    if k == 1:
        print(0)
        return

    def count():
        visit = [0] * (n+1)
        res = 0

        for i in range(1, n+1):
            if visit[i] == 0:
                res += 1
                visit[i] = 1
                dfs = [i]
                while dfs:
                    now = dfs.pop()
                    for next in graph[now]:
                        if visit[next] == 0:
                            visit[next] = 1
                            dfs.append(next)
        return res

    for i, (a, b) in enumerate(link, start = 1):
        graph[a].remove(b)
        graph[b].remove(a)
        if count() == k:
            print(i)
            return

solution()
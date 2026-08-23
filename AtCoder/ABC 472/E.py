from collections import deque

def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    check = [-1] * (n+1)
    depth = [0] * (n+1)
    check[1] = 0
    depth[1] = 1
    link = [i for i in range(n+1)]
    bfs = deque([1])
    while bfs:
        now = bfs.popleft()
        for next in graph[now]:
            if check[next] == -1:
                check[next] = 1^check[now]
                link[next] = now
                depth[next] = depth[now] + 1
                bfs.append(next)
            elif check[next] == check[now]:
                cw, ccw = [], []
                a, b = now, next
                while a != b:
                    if depth[a] > depth[b]:
                        cw.append(a)
                        a = link[a]
                    elif depth[b] > depth[a]:
                        ccw.append(b)
                        b = link[b]
                    else:
                        cw.append(a)
                        ccw.append(b)
                        a, b = link[a], link[b]
                cw.append(a)
                ccw.reverse()
                cw += ccw
                print(len(cw))
                print(*cw)
                return
    print(-1)
    return

t = int(input())
for _ in range(t):
    solution()
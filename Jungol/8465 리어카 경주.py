import sys
from collections import deque
input = sys.stdin.readline

def solution():
    mod = int(1e9)
    n, m = map(int, input().split())
    incom = [0] * (n+1)
    graph = [dict() for _ in range(n+1)]
    dp = [0] * (n+1)

    for _ in range(m):
        a, b = map(int, input().split())
        incom[b] += 1
        if b in graph[a]:
            graph[a][b] += 1
        else:
            graph[a][b] = 1

    # bfs로 2까지 도달 가능한지 확인
    bfs = deque([1])
    check = [0] * (n+1)
    check[1] = 1
    while bfs:
        now = bfs.popleft()
        for next in graph[now]:
            if check[next] == 0:
                check[next] = 1
                bfs.append(next)

    # 도달할 수 없는 경우 0 출력
    if check[2] == 0:
        print(0)
        return

    # 단순 위상정렬만으로는 사이클이 경로를 무한대로 만드는지 알 수 없음
    # incom이 0이 되지 않는 지점이 존재해도 1 -> 2에 이르는 경로가 유한한 그래프가 있음
    # 단순 경로 바깥에 사이클이 있고, 단순 경로에서 사이클로 진입할 수 없는 경우는 경로가 유한함
    no_incom = deque()
    sorted_graph = []
    for i in range(1, n+1):
        if incom[i] == 0:
            no_incom.append(i)
    while no_incom:
        node = no_incom.popleft()
        sorted_graph.append(node)
        for next in graph[node]:
            incom[next] -= graph[node][next]
            if incom[next] == 0:
                no_incom.append(next)
    if incom[2]:
        print('inf')
        return

    # check 배열로 dp[2] 값이 탐색 된 적이 없어서 0인 건지
    # mod 결과 0이 된건지 확인
    check = [0] * (n+1)
    for now in sorted_graph:
        check[now] = 1
        for next in graph[now]:
            dp[next] += dp[now]
            dp[next] %= mod
    if check[2] == 0:
        print(0)
    else:
        print(dp[2]%mod)
    return

solution()
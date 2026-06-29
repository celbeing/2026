def solution():
    l = int(input())
    n = int(input())
    r = list(map(int, input().split()))
    t = list(map(int, input().split())) +[0]

    # 출발위치: -1
    # 정비소: 0~n-1
    # 도착위치: n
    # r[i]: 정비소 i-1에서 정비소 i까지의 거리
    # t[i]: 정비소 i에서의 정비 시간

    INF = float('inf')
    dp = [INF] * (n+2)
    dp[-1] = 0
    route = [i for i in range(n+1)]

    for i in range(n+1):
        dist = r[i]
        for j in range(i-1, -2, -1):
            if dist > l: break

            if dp[i] > dp[j] + t[i]:
                dp[i] = dp[j] + t[i]
                route[i] = j
            dist += r[j]
    res = []
    k = route[n]
    while k >= 0:
        res.append(k+1)
        k = route[k]
    if res:
        res.reverse()
        print(dp[n])
        print(len(res))
        print(*res)
    else:
        print(0)
solution()
def solution():
    l = int(input())
    n = int(input())
    r = list(map(int, input().split()))
    t = [0] + list(map(int, input().split()))

    INF = float('inf')
    dp = [INF] * (n + 1)
    route = [i for i in range(n + 1)]

    dist = 0
    s, e = 0, 0
    while dist
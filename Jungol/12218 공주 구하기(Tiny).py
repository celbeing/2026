from heapq import heappush, heappop
n = int(input())
island = [tuple(map(int, input().split())) for _ in range(n)]
island.sort()

link = [[] for _ in range(n)]
for i in range(n):
    a, d, s = island[i]
    if s == 1:
        for j in range(i-1, -1, -1):
            if a-island[j][0] > d:
                break
            link[i].append(j)
    for j in range(i+1, n):
        if island[j][0]-a > d:
            break
        link[i].append(j)

res = 0
dp = [0] * (1<<n)
dp[1] = 1

ys = 1<<n
hp = ys>>1
hq = [(0, 1)]
check_forward = [0] * n
check_backward = [0] * n
while hq:
    now, bit = heappop(hq)
    if bit & hp:
        if bit & 1<<now or check_backward[now]: continue
        for next in link[now]:
            if now > next:
                if next == 0:
                    res += dp[bit]
                dp[bit|1<<next] += dp[bit]
                heappush(hq, (next, bit|1<<next))
                check_backward[now] = 1
    else:
        if check_forward[now]: continue
        for next in link[now]:
            if now < next:
                dp[bit|1<<next] += dp[bit]
                heappush(hq, (next, bit|1<<next))
                check_forward[now] = 1

print(res)

# gpt에 물어본 거 남아있음
pre = [0] * 1000000
n = int(input())
for _ in range(n):
    s, v = map(int, input().split())
    pre[s] += v


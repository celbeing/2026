import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    max_h = [0] * 40001
    for _ in range(n):
        w, h = map(int, input().split())
        max_h[w] = max(max_h[w], h)

    res = 0
    t = 0
    for i in range(40000, 0, -1):
        t = max(t, max_h[i])
        res += t
    print(res)

solution()
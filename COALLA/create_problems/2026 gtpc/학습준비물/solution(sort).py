import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    paper = [tuple(map(int, input().split())) for _ in range(n)]
    paper.sort()
    paper.reverse()

    res = 0
    t = 0
    for w, h in paper:
        if h > t:
            res += (h-t)*w
            t = h
    print(res)

solution()
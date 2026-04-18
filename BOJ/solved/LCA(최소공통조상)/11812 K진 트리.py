import sys
input = sys.stdin.readline

def solution():
    n, k, q = map(int, input().split())
    if k == 1:
        for _ in range(q):
            x, y = map(int, input().split())
            print(abs(x - y))
    else:
        for _ in range(q):
            x, y = map(int, input().split())
            x -= 1; y -= 1
            step = 0
            while x != y:
                if x > y:
                    x -= 1
                    x //= k
                else:
                    y -= 1
                    y //= k
                step += 1
            print(step)

solution()
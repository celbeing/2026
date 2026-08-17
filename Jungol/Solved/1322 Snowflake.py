import sys
input = sys.stdin.readline

def solution():
    def func(a):
        ls = []
        for i in range(6):
            p = a[i:]+a[:i]
            ls.append(tuple(p))
            ls.append(tuple(reversed(p)))
        ls.sort()
        return ls[0]

    n = int(input())
    check = set()
    for _ in range(n):
        a = func(list(map(int, input().split())))
        if a in check:
            print('Twin snowflakes found.')
            return
        check.add(a)
    print('No two snowflakes are alike.')
    return

solution()
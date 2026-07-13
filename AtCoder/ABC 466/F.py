import sys
sys.setrecursionlimit(200000)

def solution():
    N, X = map(int, input().split())
    a = [10**18]
    for k in list(map(int, input().split())):
        if k < a[-1]:
            a.append(k)

    memo = dict()

    def func(i, x):
        if x < 0: return 0
        if i == len(a): return 1

        if (i, x) in memo:
            return memo[(i, x)]
        q = (x+1)//a[i]
        r = (x+1)%a[i]
        res = func(i+1, a[i]-1)*q+func(i+1, r-1)
        return res

    print(func(1, X)-1)

t = int(input())
for _ in range(t):
    solution()
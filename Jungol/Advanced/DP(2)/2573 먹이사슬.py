import sys
from bisect import bisect_left

input = sys.stdin.readline

def solution():
    n = int(input())
    check = set()
    for _ in range(n):
        i, l, r = map(int, input().split())
        if (l, r) in check: continue
        check.add((l, r))
    animal = sorted(check, key=lambda x:(x[1], -x[0]))
    del check
    left = sorted(l for l, r in animal)
    n = len(left)

    fw = [0] * (n+1)

    def fw_update(i, x):
        while i <= n:
            fw[i] = max(fw[i], x)
            i += i&-i

    def fw_query(k):
        res = 0
        while k:
            res = max(res, fw[k])
            k -= k&-k
        return res
    ans = 0
    for l, r in animal:
        idx = n - bisect_left(left, l)
        res = fw_query(idx)+1
        fw_update(idx, res)
        ans = max(ans, res)

    print(ans)
solution()
import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    a = set()
    a.update(list(map(int, input().split())))
    b = sorted(list(a))
    res = 0
    lim = b[0] // 4

    def L_check(k):
        if k > lim: return 0
        count = 0
        check = set()
        for t in b:
            if t % k in check:
                continue
            else:
                count += 1
                if count > 3:
                    return 0
                check.add(t % k)
        return k

    def diff(k):
        for i in range(1, int(k ** 0.5)+1):
            if k % i == 0:
                cand.add(i)
                cand.add(k//i)

    if len(b) < 4:
        m = b[0] // 4
        res += (m + 1) * m // 2
    else:
        p,q,r,s = b[:4]
        cand = set()
        diff(s-r)
        diff(s-q)
        diff(s-p)
        diff(r-q)
        diff(r-p)
        diff(q-p)
        for c in cand:
            res += L_check(c)

    print(res)

solution()
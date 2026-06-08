import sys
input = sys.stdin.readline

def solution():
    m, k = map(int, input().split())
    a = list(map(int, input().split()))

    def check(t):
        ret = 0
        count = 0
        for p in a:
            if count+p > t:
                ret += 1
                count = 0
            count += p
        if count:
            ret += 1

        return True if ret <= k else False

    s, e = max(a), sum(a)
    result = e
    while s <= e:
        m = (s+e)//2
        if check(m):
            result = m
            e = m - 1
        else:
            s = m + 1

    answer = []
    count = 0
    k -= 1
    for p in reversed(a):
        if count + p > result:
            answer.append('/')
            count = 0
            k -= 1
        answer.append(str(p))
        count += p
    answer.reverse()
    idx = 0
    while k:
        if answer[idx] != '/' and answer[idx+1] != '/':
            idx += 1
            answer.insert(idx, '/')
            k -= 1
        idx += 1

    print(' '.join(answer))

solution()
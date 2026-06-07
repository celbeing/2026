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
    while s < e:
        m = (s+e)//2
        if check(m):
            result = m
            e = m - 1
        else:
            s = m + 1

    # k명의 서기공이 모두 일을 해야 함
    # 출력 구분 수가 k보다 작은 경우 있음
    answer = []
    count = 0
    for p in a:
        if count + p > result:
            answer.append('/')
            count = 0
        answer.append(str(p))
        count += p
    print(' '.join(answer))

solution()
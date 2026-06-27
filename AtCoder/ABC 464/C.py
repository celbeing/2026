def solution():
    n, m = map(int, input().split())
    count = dict()
    res = 0
    birds = []
    for _ in range(n):
        a, d, b = map(int, input().split())
        birds.append((d, a, b))
        if a in count:
            count[a] += 1
        else:
            count[a] = 1
            res += 1
    birds.sort()
    idx = 0
    for day in range(1, m+1):
        while idx < n and birds[idx][0] == day:
            d, a, b = birds[idx]
            count[a] -= 1
            if count[a] == 0:
                res -= 1

            if b in count:
                count[b] += 1
            else:
                count[b] = 1
            if count[b] == 1:
                res += 1
            idx += 1
        print(res)

solution()
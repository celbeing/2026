res = 0
n, q = map(int, input().split())
count = dict()
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        if x in count:
            res ^= count[x]
            count[x] += 1
            res ^= count[x]
        else:
            res ^= 1
            count[x] = 1
    else:
        d = []
        for x in count:
            res ^= count[x]
            count[x] -= 1
            res ^= count[x]
            if count[x] == 0:
                d.append(x)
        for x in d:
            del count[x]
    print(res)
def solution():
    h, w, q = map(int, input().split())
    grid = [bytearray(b'A' * w) for _ in range(h)]
    query = []
    for _ in range(q):
        r, c, x = input().split()
        query.append((int(r), int(c), ord(x)))
    query.reverse()

    conq = [0]*h
    for r, c, x in query:
        s, e = 0, h
        while s < e:
            m = (s+e)//2
            if conq[m] > c-1:
                s = m+1
            else:
                e = m
        for i in range(s, r):
            grid[i][conq[i]:c] = bytes([x])*(c-conq[i])
            conq[i] = c
    print('\n'.join(g.decode() for g in grid))
solution()
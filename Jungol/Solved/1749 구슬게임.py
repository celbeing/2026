def solution():
    B = list(map(int, input().split()))
    grundy = [0] * 501
    for i in range(B[0], 501):
        link = set()
        for b in B:
            if b > i: break
            link.add(grundy[i-b])
        for j in range(4):
            if not(j in link):
                grundy[i] = j
                break
    for _ in range(5):
        p, q = map(int, input().split())
        if grundy[p] ^ grundy[q]: print('A')
        else: print('B')
solution()
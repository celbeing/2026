import sys
input = sys.stdin.readline

def solution():
    n, q = map(int, input().split())
    size = 1
    while size < n:
        size <<= 1
    seg = [0] * size * 2
    # l,r end: 구간의 양 쪽 끝이 0인지 확인
    l_end = [0] * size * 2
    r_end = [0] * size * 2
    for i in range(n):
        seg[size+i] = 1
        l_end[size+i] = 1
        r_end[size+i] = 1
    for i in range(size-1,0,-1):
        l_end[i] = l_end[i*2]
        r_end[i] = r_end[i*2+1]
        seg[i] = seg[i*2]+seg[i*2+1]
        if r_end[i*1] & l_end[i*2+1]:
            seg[i] -= 1


    h = list(map(int, input().split()))
    h_sorted = []
    for i, hh in enumerate(h):
        h_sorted.append((hh, i))
    h_sorted.sort()
    query = []
    for i in range(q):
        l, r, x = map(int, input().split())
        query.append((x, l, r, i))
    query.sort()

    idx = 0
    result = []
    for x, l, r, i in query:
        while idx < n and h_sorted[idx][0] <= x:
            t = h_sorted[idx][1]
            h[t] = 0
            t += size
            seg[t] = 0
            r_end[t] = 0
            l_end[t] = 0
            t >>= 1
            while t:
                l_end[t] = l_end[t*2]
                r_end[t] = r_end[t*2+1]
                seg[t] = seg[t*2]+seg[t*2+1]
                if r_end[t*2] and l_end[t*2+1]: seg[t] -= 1
                t >>= 1
            idx += 1
        l += size-1
        r += size-1
        left = []
        right = []
        while l < r:
            if l & 1:
                left.append(l)
                l += 1
            l >>= 1
            if not(r & 1):
                right.append(r)
                r -= 1
            r >>= 1
        if l == r:
            left.append(l)
        right.reverse()
        left += right

        count = seg[left[0]]
        for j in range(1, len(left)):
            count += seg[left[j]]
            if r_end[left[j-1]] & l_end[left[j]]:
                count -= 1

        result.append((i, count))
    result.sort()

    for i, res in result:
        print(res)

solution()
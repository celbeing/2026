def solution():
    s = input().strip()
    size = 1
    while size < len(s):
        size <<= 1

    seg = [0] * size * 2
    pre_seg = [0] * size * 2
    r_cnt = 0

    for i in range(len(s)):
        if s[i] == 'L':
            seg[size+i] = 1
            pre_seg[size+i] = 1
        elif s[i] == 'R':
            seg[size+i] = -1
            pre_seg[size+i] = -1
            r_cnt += 1

    for i in range(size-1, 0, -1):
        seg[i] = seg[i*2]+seg[i*2+1]
        pre_seg[i] = max(pre_seg[i*2], seg[i*2]+pre_seg[i*2+1])

    for _ in range(int(input())):
        p, c = input().split()
        p = size+int(p)-1
        c = 1 if c == 'L' else -1
        if seg[p] == c:
            print(pre_seg[1] + r_cnt)
            continue
        elif seg[p] > c: r_cnt += 1
        else: r_cnt -= 1

        seg[p] = c
        pre_seg[p] = c
        p >>= 1
        while p:
            seg[p] = seg[p*2]+seg[p*2+1]
            pre_seg[p] = max(pre_seg[p*2], seg[p*2]+pre_seg[p*2+1], 0)
            p >>= 1
        print(pre_seg[1] + r_cnt)

solution()
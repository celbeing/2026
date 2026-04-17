import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
c = [0] * n
for i in range(n - 2):
    c[i] = a[i] + a[i + 2] - a[i + 1] * 2

size = 1
while size < n:
    size <<= 1

left_seg = [0] * size * 2
right_seg = [0] * size * 2
total_seg = [0] * size * 2
all_seg = [1] * size * 2
len_seg = [0] * size * 2

for i in range(n-2):
    if c[i] == 0:
        left_seg[size + i] = 1
        right_seg[size + i] = 1
        total_seg[size + i] = 1
    else:
        all_seg[size + i] = 0
    len_seg[size + i] = 1
for i in range(size - 1, 0, -1):
    len_seg[i] = len_seg[i*2]+len_seg[i*2]
    left_seg[i] = left_seg[i * 2]
    if all_seg[i * 2]: left_seg[i] += left_seg[i * 2 + 1]
    right_seg[i] = right_seg[i * 2 + 1]
    if all_seg[i * 2 + 1]: right_seg[i] += right_seg[i * 2]
    total_seg[i] = max(total_seg[i*2], total_seg[i*2+1], right_seg[i * 2] + left_seg[i * 2 + 1])
    if total_seg[i] != len_seg[i]: all_seg[i] = 0


def update(t, idx):
    if c[t]:
        left_seg[idx] = 0
        right_seg[idx] = 0
        total_seg[idx] = 0
        all_seg[idx] = 0
    else:
        left_seg[idx] = 1
        right_seg[idx] = 1
        total_seg[idx] = 1
        all_seg[idx] = 1
    idx >>= 1
    while idx:
        left_seg[idx] = left_seg[idx * 2]
        if all_seg[idx * 2]: left_seg[idx] += left_seg[idx * 2 + 1]
        right_seg[idx] = right_seg[idx * 2 + 1]
        if all_seg[idx * 2 + 1]: right_seg[idx] += right_seg[idx * 2]
        total_seg[idx] = max(total_seg[idx*2], total_seg[idx*2+1], right_seg[idx * 2] + left_seg[idx * 2 + 1])
        if total_seg[idx] != len_seg[idx]: all_seg[idx] = 0
        else: all_seg[idx] = 1
        idx >>= 1


for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        i, j, x, y = q[1:]
        if 2 < i:
            c[i - 3] += x
            update(i - 3, size + i - 3)
        if 1 < i:
            c[i - 2] += y - x
            update(i - 2, size + i - 2)
        if 1 < j:
            c[j - 2] -= x + y * (j - i + 1)
            update(j - 2, size + j - 2)
        c[j - 1] += x + y * (j - i)
        update(j - 1, size + j - 1)
    else:
        i, j = q[1:]
        i += size - 1
        j += size - 3
        node = []
        merge = []

        while i < j:
            if i & 1:
                node.append(i)
                i += 1
            i >>= 1
            if not (j & 1):
                merge.append(j)
                j -= 1
            j >>= 1
        if i == j:
            node.append(i)
        node += reversed(merge)

        streak = 0
        res = 0
        for k in node:
            if all_seg[k]:
                streak += total_seg[k]
                res = max(res, streak)
            elif left_seg[k]:
                streak += left_seg[k]
                res = max(res, streak, total_seg[k])
                streak = right_seg[k]
            else:
                res = max(res, total_seg[k])
                streak = right_seg[k]

        res += 2
        print(res)
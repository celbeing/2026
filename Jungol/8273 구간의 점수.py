import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    size = 1
    while size < n:
        size <<= 1
    sum_seg = [0] * size * 2
    min_seg = [1000001] * size * 2
    idx_seg = [0] * size * 2
    a = list(map(int, input().split()))
    for i in range(n):
        sum_seg[i+size] = a[i]
        min_seg[i+size] = a[i]
        idx_seg[i+size] = i
    for i in range(size-1, 0, -1):
        sum_seg[i] = sum_seg[i*2]+sum_seg[i*2+1]
        min_seg[i] = min(min_seg[i*2],min_seg[i*2+1])
        idx_seg[i] = idx_seg[i*2] if min_seg[i*2] <= min_seg[i*2+1] else idx_seg[i*2+1]

    def get_score(s,e):
        score = 0
        res_l, res_r = s, e
        l, r = s+size, e+size

        part_sum = 0
        part_min = 1000001
        part_idx = -1
        while l < r:
            if l & 1:
                part_sum += sum_seg[l]
                if min_seg[l] < part_min:
                    part_min = min_seg[l]
                    part_idx = idx_seg[l]
                


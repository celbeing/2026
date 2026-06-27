def solution():
    n = int(input())
    s = input().strip()
    now = 1
    count = 0
    start = 0
    wrong = 0
    for i in range(n):
        k = 1 if s[i] == 'S' else 0
        if now == k:
            count += 1
        else:
            count = 1
            if k == 1: start += 1
            now ^= 1
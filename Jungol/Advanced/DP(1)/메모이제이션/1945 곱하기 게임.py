def solution():
    n = int(input())
    p = 1
    while p < n:
        p *= 9
        if p >= n:
            print('Stan wins.')
            break
        p <<= 1
        if p >= n:
            print('Ollie wins.')
            break
solution()
def solution():
    a, b, c, d = map(int, input().split())
    p, q, r, s = map(int, input().split())
    if a > r or b > s or p > c or q > d: print('NULL')
    elif (c==p and d==q) or (a==r and b==s) or (a==r and d==q) or (c==p and b==s): print('POINT')
    elif a==r or c==p or b==s or d==q: print('LINE')
    else: print('FACE')
solution()
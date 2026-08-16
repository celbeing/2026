n, m = map(int, input().split())
if n == m == 1: print('YES')
else:
    even, odd = set(), set()
    for i in range(n):
        a = list(map(int, input().split()))
        if i & 1:
            even.update(a[1::2])
            odd.update(a[0::2])
        else:
            even.update(a[0::2])
            odd.update(a[1::2])
        if even&odd:
            print('YES')
            break
    else:
        print('NO')
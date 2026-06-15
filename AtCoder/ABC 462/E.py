for _ in range(int(input())):
    a, b, x, y = map(int, input().split())
    x, y = abs(x), abs(y)
    res = min(a, b) * min(x, y) * 2
    if x != y:
        rem = abs(x-y) // 2
        if abs(x-y)&1:
            if x > y:
                res += min(rem*(a+b)+a, rem*a*4+a, rem*b*4+b*3)
            else:
                res += min(rem*(a+b)+b, rem*b*4+b, rem*a*4+a*3)
        else:
            if max(a, b) > min(a, b)*3:
                res += rem * 4 * min(a, b)
            else:
                res += rem*(a+b)
    print(res)
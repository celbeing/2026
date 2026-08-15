a, b = map(int, input().split())
c = (a+b, a-b, a*b, 9 if a == b*9 else 0)
if 9 in c:
    print('Nine')
else:
    print('Nein')

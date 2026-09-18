n = int(input())
a = n//25
b = n%25
res = 'A'*a+'C'*(25-b)+'A'+'C'*b
print('R'.join(res))
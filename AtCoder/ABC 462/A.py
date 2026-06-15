S = input().strip()
res = ''
digit = '0123456789'
for s in S:
    if s in digit: res += s
print(res)
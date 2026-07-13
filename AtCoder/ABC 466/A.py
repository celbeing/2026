n = int(input())
x = list(map(int, input().split()))
flag = True
for a in x:
    if a >= 0:
        flag = False
        break
print('Yes' if flag else 'No')
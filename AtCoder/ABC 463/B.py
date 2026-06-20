n, x = input().split()
if x == 'A': x = 0
elif x == 'B': x = 1
elif x == 'C': x = 2
elif x == 'D': x = 3
else: x = 4
for _ in range(int(n)):
    s = input()
    if s[x] == 'o':
        print('Yes')
        break
else:
    print('No')
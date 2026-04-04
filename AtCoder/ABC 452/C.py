import sys
input = sys.stdin.readline

n = int(input())
rib = []
for _ in range(n):
    a, b = map(int, input().split())
    rib.append((a, b-1))
m = int(input())
strings = []
check = [set() for _ in range(n)]

for _ in range(m):
    s = input().strip()
    strings.append(s)
    l = len(s)
    cnt = 0
    for a, b in rib:
        if l == a:
            check[cnt].add(s[b])
        cnt += 1

for s in strings:
    flag = True
    if len(s) == n:
        for i in range(n):
            if s[i] in check[i]:
                continue
            else:
                flag = False
                break

    else:
        flag = False
    print('Yes' if flag else 'No')
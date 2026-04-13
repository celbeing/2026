import sys

t, x = map(int, input().split())
a = list(map(int, input().split()))
last = a[0]
print(0, last)
for i in range(1, t+1):
    if abs(last - a[i]) >= x:
        last = a[i]
        print(i, last)
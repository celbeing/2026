import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))
for k in a:
    if x > k:
        print(1)
        x = k
    else:
        print(0)
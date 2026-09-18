import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()

    if sum(a) == 0:
        print(0)
    else:
        cnt = 1
        for i in range(1, n):
            if a[i-1]*2 > a[i]:
                cnt = -1
                break
            else:
                cnt = max(cnt, a[i]-a[i-1]*2)
        print(cnt)
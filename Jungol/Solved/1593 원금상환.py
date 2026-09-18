import sys
input = sys.stdin.readline

n = int(input())
prefix = 0
back = 0
dist = 0

for i in range(1, n+1):
    prefix += int(input())
    if back == 0 and prefix < 0:
        back = i
    elif back and prefix >= 0:
        dist += i-back
        back = 0

dist *= 2
dist += n

print(dist)
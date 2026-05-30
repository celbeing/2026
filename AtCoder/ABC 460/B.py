import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x,y,r,a,b,d = map(int, input().split())
    dist = (x-a)**2 + (y-b)**2
    if dist > (r+d)**2:
        print('No')
    elif dist**0.5+min(r,d) < max(r,d):
        print('No')
    else:
        print('Yes')
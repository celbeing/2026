import sys
input = sys.stdin.readline

m, d = map(int, input().split())
seasonal_fest = {(1,7), (3, 3), (5, 5), (7, 7), (9, 9)}
if (m, d) in seasonal_fest:
    print('Yes')
else:
    print('No')
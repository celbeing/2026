import sys
input = sys.stdin.readline
n = int(input())
res = [i for i in range(n, 0, -1)]
res = list(map(str, res))
print(','.join(res))
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

size = 1
while size < n:
    size <<= 1

seg = [0] * size * 2
l_max = [0] * size * 2
r_max = [0] * size * 2
t_max = [0] * size * 2

for i in range(n):
    seg[size+i] = arr[i]
    l_max[size+i] = arr[i]
    r_max[size+i] = arr[i]
    t_max[size+i] = arr[i]
for i in range(size, 0, -1):
    seg[i] = seg[i*2] + seg[i*2+1]
    l_max[i] = max(l_max[i*2], seg[i*2] + l_max[i*2+1])
    r_max[i] = max(r_max[i*2+1], seg[i*2+1] + r_max[i*2])
    t_max[i] = max(max(t_max[i*2], t_max[i*2+1]), r_max[i*2] + l_max[i*2+1])

for _ in range(int(input())):
    i, j = map(int, input().split())
    
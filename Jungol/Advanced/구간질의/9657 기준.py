import sys
input = sys.stdin.readline

n = int(input())
stu = []
v_set = set()
v_map = dict()

for i in range(n):
    v, a = map(int, input().split())
    v_set.add(v)
    stu.append((v, a))

v_list = sorted(list(v_set))
l = len(v_list)
for i, v in enumerate(v_list):
    v_map[v] = i

size = 1
while size < l:
    size <<= 1
seg = [0] * size * 2
for v, a in stu:
    idx = v_map[v]+size
    while idx:
        seg[idx] += a
        idx >>= 1
    l, r = 0, 0
    idx = 1
    while idx < size:
        if l + seg[idx*2] >= r + seg[idx*2+1]:
            r += seg[idx*2+1]
            idx <<= 1
        else:
            l += seg[idx*2]
            idx <<= 1
            idx += 1
    print(v_list[idx-size])
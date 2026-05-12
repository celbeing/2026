s = input().strip()
size = 1
while size < len(s):
    size <<= 1

seg_l = [0] * size * 2
seg_r = [0] * size * 2
cnt = [0] * size * 2
lazy = [0] * size * 2

for i in range(len(s)):

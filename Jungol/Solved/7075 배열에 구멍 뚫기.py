n = int(input())
INF = -float('inf')
size = 1
while size < n:
    size <<= 1
seg = [0] * size * 2
seg_l = [0] * size * 2
seg_r = [0] * size * 2
seg_t = [0] * size * 2

a = list(map(int, input().split()))
for i in range(n):
    seg[size+i] = a[i]
    seg_l[size+i] = a[i]
    seg_r[size+i] = a[i]
    seg_t[size+i] = a[i]
for i in range(size-1,0,-1):
    seg[i] = seg[i*2]+seg[i*2+1]
    seg_l[i] = max(seg_l[i*2], seg[i*2]+seg_l[i*2+1])
    seg_r[i] = max(seg_r[i*2+1], seg_r[i*2]+seg[i*2+1])
    seg_t[i] = max(seg_t[i*2],seg_t[i*2+1],seg_r[i*2]+seg_l[i*2+1])

for k in list(map(int, input().split())):
    k += size-1
    seg[k] = INF
    seg_l[k] = INF
    seg_r[k] = INF
    seg_t[k] = INF
    k >>= 1
    while k:
        seg[k] = seg[k*2]+seg[k*2+1]
        seg_l[k] = max(seg_l[k*2], seg[k*2]+seg_l[k*2+1])
        seg_r[k] = max(seg_r[k*2+1], seg_r[k*2]+seg[k*2+1])
        seg_t[k] = max(seg_t[k*2],seg_t[k*2+1],seg_r[k*2]+seg_l[k*2+1])
        k >>= 1
    print(seg_t[1] if seg_t[1] > 0 else 0)
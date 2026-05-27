import sys
from bisect import bisect_right
input = sys.stdin.readline

n = int(input())
p = [0] + [int(input()) for _ in range(n)]
parent = [0] * (n+1)
children = [[] for _ in range(n+1)]
for i in range(2, n+1):
    k = int(input())
    parent[i] = k
    children[k].append(i)

# node에 대한 dfs 진입 순서와 종료 순서(sub_tree를 모두 순회했을 때 dfs_count)
dfs_in = [0] * (n+1)
dfs_out = [0] * (n+1)
dfs_order = []

stack = [(1, 0)]
while stack:
    now, is_root = stack.pop()
    if is_root == 0:
        dfs_in[now] = len(dfs_order)
        dfs_order.append(now)
        stack.append((now, 1))
        for next in reversed(children[now]):
            stack.append((next, 0))
    else:
        dfs_out[now] = len(dfs_order)-1

stat = [0] * (n+1)
for i in range(1, n+1):
    stat[dfs_in[i]] = p[i]


# merge sort tree 구성
size = 1
while size < n:
    size <<= 1
mst = [[] for _ in range(size*2)]

for i in range(n):
    mst[size+i] = [stat[i]]

for i in range(size-1,0,-1):
    left = mst[i*2]
    right = mst[i*2+1]
    merge = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merge.append(left[l])
            l += 1
        else:
            merge.append(right[r])
            r += 1
    merge += left[l:]
    merge += right[r:]
    mst[i] = merge

def query(l, r, x):
    l, r = l + size, r + size
    res = 0
    while l <= r:
        if l & 1:
            res += len(mst[l])-bisect_right(mst[l],x)
            l += 1
        if not(r & 1):
            res += len(mst[r])-bisect_right(mst[r],x)
            r -= 1
        l >>= 1
        r >>= 1
    return str(res)

answer = [query(dfs_in[i], dfs_out[i], p[i]) for i in range(1, n+1)]
print('\n'.join(answer))
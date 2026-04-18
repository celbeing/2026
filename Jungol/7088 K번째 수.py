import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
size = 1
while size < n:
    size <<= 1

tree = [[] for _ in range(size * 2)]
for i in range(n):
    tree[size+i].append(a[i])
for i in range(size-1,0,-1):
    l, r = 0, 0
    while l < len(tree[i*2]) and r < (len(tree[i*2+1])):
        if tree[i*2][l] < tree[i*2+1][r]:
            tree[i].append(tree[i*2][l])
            l += 1
        else:
            tree[i].append(tree[i*2+1][r])
            r += 1
    while l < len(tree[i*2]):
        tree[i].append(tree[i*2][l])
        l += 1
    while r < len(tree[i*2+1]):
        tree[i].append(tree[i*2+1][r])
        r += 1

def bin_search(arr, k):
    s, e = 0, len(arr)
    while s < e:
        m = (s+e)//2


'''
def merge_sort(left, right):
    l, r = 0, 0
    ret = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            ret.append(left[l])
            l += 1
        else:
            ret.append(right[r])
            r += 1
    while l < len(left):
        ret.append(left[l])
        l += 1
    while r < len(right):
        ret.append(right[r])
        r += 1
    return ret

for _ in range(m):
    i,j,k = map(int, input().split())
    i += size-1; j += size-1; k -= 1
    left, right = [], []
    while i < j:
        if i & 1:
            left = merge_sort(left, tree[i])
            i += 1
        i >>= 1
        if not(j & 1):
            right = merge_sort(right, tree[j])
            j -= 1
        j >>= 1
    if i == j:
        left = merge_sort(left, tree[i])
    print(merge_sort(left, right)[k])
'''
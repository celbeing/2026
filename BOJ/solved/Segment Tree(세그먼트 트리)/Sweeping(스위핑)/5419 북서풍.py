import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    island = []
    coor_check = set()
    for _ in range(n):
        x, y = map(int, input().split())
        island.append((x, -y))
        coor_check.add(-y)
    k = len(coor_check)

    coor_check = sorted(list(coor_check))
    island.sort()
    code = dict()
    for i in range(k):
        code[coor_check[i]] = i

    size = 1
    while size < k:
        size <<= 1

    seg = [0] * size * 2

    def query(node, start, end, left, right):
        if end < left or right < start: return 0
        if left <= start and end <= right: return seg[node]

        mid = (start + end) // 2
        return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

    def update(node, start, end, tar):
        seg[node] += 1
        if start == end:
            return

        mid = (start + end) // 2
        if tar <= mid:
            update(node*2, start, mid, tar)
        else:
            update(node*2+1, mid+1, end, tar)
        return

    result = 0

    for x, y in island:
        ny = code[y]
        result += query(1, 1, k, 1, ny + 1)
        update(1, 1, k, ny + 1)

    print(result)
    return

for _ in range(int(input())):
    solution()
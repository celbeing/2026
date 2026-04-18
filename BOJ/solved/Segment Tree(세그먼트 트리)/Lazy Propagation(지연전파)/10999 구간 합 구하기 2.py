import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

seg = [0] * n * 4
lazy = [0] * n * 4

# 트리 초기화
def init_tree(arr, node, start, end):
    # 리프에 도달
    if start == end:
        seg[node] = arr[start - 1]

    # 하위 노드 탐색
    else:
        mid = (start + end) // 2
        init_tree(arr, node * 2, start, mid)
        init_tree(arr, node * 2 + 1, mid + 1, end)
        seg[node] = seg[node * 2] + seg[node * 2 + 1]
    return seg[node]

# 구간합을 구하는 쿼리
def query(node, start, end, left, right):
    push(node, start, end)
    if end < left or right < start:
        return 0

    if left <= start and end <= right:
        return seg[node]

    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)

# lazy 트리의 값을 seg 트리에 반영
def push(node, start, end):
    if lazy[node] != 0:
        seg[node] += (end - start + 1) * lazy[node]

        # 리프가 아닌 경우, 하위 노드로 전파
        if start < end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0
    return

# 구간의 값을 변경하는 쿼리
def update(node, start, end, left, right, w):
    push(node, start, end)
    if end < left or right < start:
        return

    # 현재 구간이 쿼리 구간에 완전히 포함되는 경우
    # lazy 트리에 반영하여 하위 노드에 전파를 지연함
    if left <= start and end <= right:
        lazy[node] += w
        push(node, start, end)
        return

    # 양쪽 노드로 이어서 쿼리 탐색
    mid = (start + end) // 2
    update(node * 2, start, mid, left, right, w)
    update(node * 2 + 1, mid + 1, end, left, right, w)

    # seg 트리의 값 갱신
    seg[node] = seg[node * 2] + seg[node * 2 + 1]
    return
a = [int(input()) for _ in range(n)]
init_tree(a, 1, 1, n)

for _ in range(m + k):
    q = list(map(int, input().split()))
    if q[0] == 1:
        update(1, 1, n, q[1], q[2], q[3])
    else:
        print(query(1, 1, n, q[1], q[2]))
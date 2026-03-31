import sys
input = sys.stdin.readline

n = int(input())
seg = [0] * n * 4
lazy = [0] * n * 4
a = list(map(int, input().split()))

# 트리 초기화
def init_tree(arr, node, start, end):
    # 리프에 도달하면 값 저장
    if start == end:
        seg[node] = arr[start-1]
        return

    # 하위 노드로 이동
    mid = (start + end) // 2
    init_tree(arr, node*2, start, mid)
    init_tree(arr, node*2+1, mid+1, end)

    # 현재 노드 업데이트
    seg[node] = seg[node*2] ^ seg[node*2+1]
    return

# 구간 xor 쿼리
def query(node, start, end, left, right):
    # 갱신되지 않은 값이 있으면 push
    if lazy[node]: push(node, start, end)

    # 쿼리 범위를 벗어난 경우
    if end < left or right < start:
        return 0

    # 쿼리 구간에 모두 포함되는 경우
    if left <= start and end <= right:
        return seg[node]    # 이미 push 되어있기 때문에 모든 쿼리가 반영되어있음

    # 하위 쿼리를 호출
    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) ^ query(node*2+1, mid+1, end, left, right)

# 구간 xor 업데이트
def update(node, start, end, left, right, k):
    # 갱신되지 않은 값이 있으면 push
    if lazy[node]: push(node, start, end)

    # 쿼리 구간을 벗어난 경우
    if end < left or right < start:
        return

    # 쿼리 구간에 모두 포함되는 경우
    if left <= start and end <= right:
        # 리프의 수가 홀수 개인 경우만 현재 노드에 xor 반영
        if (end - start + 1) & 1:
            seg[node] ^= k

        # 하위 노드가 있는 경우(리프가 아닌 경우)
        # 하위 노드의 쿼리는 갱신하지 않고 저장
        if start < end:
            lazy[node*2] ^= k
            lazy[node*2+1] ^= k
        return

    # 하위 쿼리를 호출
    mid = (start + end) // 2
    update(node*2, start, mid, left, right, k)
    update(node*2+1, mid+1, end, left, right, k)

    # 현재 노드의 값 갱신
    # 하위 쿼리를 실행했기 때문에 지연된 쿼리가 모두 반영되어있음
    seg[node] = seg[node*2] ^ seg[node*2+1]
    return

# 지연된 쿼리 반영
def push(node, start, end):
    # 리프의 수가 홀수 개인 경우만 현재 노드에 lazy 반영
    if (end - start + 1) & 1:
        seg[node] ^= lazy[node]

    # 리프가 아닌 경우
    # 하위 노드에 lazy 값 전파
    if start < end:
        lazy[node*2] ^= lazy[node]
        lazy[node*2+1] ^= lazy[node]

    lazy[node] = 0
    return

init_tree(a, 1, 1, n)
for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        update(1, 1, n, q[1]+1, q[2]+1, q[3])
    else:
        print(query(1, 1, n, q[1]+1, q[2]+1))
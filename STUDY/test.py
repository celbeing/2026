N = int(input())
arr = list(map(int, input().split()))

# 세그먼트 트리의 크기를 결정합니다.
# 필요한 최소 크기는 N보다 크거나 같은 가장 작은 2의 거듭제곱의 2배입니다.
size = 1
while size < N:
    size <<= 1

seg = [0] * size * 2

# arr의 값을 세그먼트 트리에 배치합니다.
# node: 세그먼트 트리의 인덱스
# start, end: 현재 node가 관리할 원본 배열 구간의 시작과 끝(1~N)
def init_tree(arr, node, start, end):
    # start, end 매개변수가 일치한다면 리프에 도달했다는 의미, 즉 구간의 길이 1입니다.
    # 배열의 값을 그대로 불러와 노드에 저장하고 return 합니다.
    if start == end:
        seg[node] = arr[start - 1]
        return

    # 현재 구간을 반으로 나누어 양쪽 자식 노드의 값을 구하러 갑니다.
    mid = (start + end) // 2
    init_tree(arr, node*2, start, mid)
    init_tree(arr, node*2+1, mid+1, end)

    # 하위 구간 값으로 현재 구간 값 구성
    # 여기서는 구간 합을 구성하는 예시를 썼습니다.
    seg[node] = seg[node*2] + seg[node*2+1]
    return

# node는 1, start와 end는 구간 전체인 1, N으로 하여 탐색을 시작합니다.
# 리프부터 상향식으로 트리가 초기화됩니다.
init_tree(arr, 1, 1, N)

# left로부터 right까지의 구간 값을 가져올 쿼리입니다.
# start와 end가 left, right를 벗어나지 않는 탐색만 실행합니다.
def query(node, start, end, left, right):
    # end가 left보다 작거나 start가 right보다 큰 경우는
    # 현재 탐색하는 node가 관리하는 구간이 쿼리 구간을 완전히 벗어났음을 의미합니다.
    # 이때는 구간 데이터에 어떤 연산을 하고 있는지에 따라 0, 1 등을 return 합니다.
    # 지금 예시로 보고 있는 세그먼트 트리는 구간 합을 관리하기 때문에 0을 return 합니다.
    if end < left or right < start:
        return 0

    # 반대로 start와 end가 [left, right] 구간에 완전히 포함되는 경우입니다.
    # 이 경우는 현재 node의 자식을 살펴볼 필요가 없습니다.
    # 현재 node에서 관리 중인 값을 그대로 return 합니다.
    if left <= start and end <= right:
        return seg[node]

    # 위의 두 분기에서 처리되지 않은 탐색은 구간이 걸친 경우입니다.
    # 좌, 우 자식 노드를 각각 쿼리하여 결과를 반환합니다.
    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)
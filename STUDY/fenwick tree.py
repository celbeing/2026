# fw_tree[i]가 관리하는 구간의 길이
def fw_len(k):
    return k&-k

# 구간합을 관리하는 fw_tree[i]의 쿼리
def fw_sum(l, r):
    return prefix_sum(r) - prefix_sum(l-1)

def prefix_sum(k):
    result = 0
    while k:
        result += fw_tree[k]    # 현재 인덱스를 누적
        k -= fw_len(k)          # 현재 인덱스가 관리하는 길이만큼 앞으로 점프
                                # 인덱스가 0을 가리키면 더 이상 더할 구간이 없음
    return result

n, q= map(int, input().split())
fw_tree = [0] * (n+1)
for i, a in enumerate(list(map(int, input().split()))):
    fw_tree[i+1] += a
    j = i + ((i+1)&-(i+1)) + 1
    if j <= n:
        fw_tree[j] += fw_tree[i+1]
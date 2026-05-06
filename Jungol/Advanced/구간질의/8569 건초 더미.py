import sys
input = sys.stdin.readline

# 좌표압축 + 세그트리 + 오프라인쿼리
# 건초 방어력을 좌표압축해서 최대 30만개로 관리
# idx: D_i로 매핑 후에 내림차순으로 세그트리 리프에 배치
# seg[i]에는 i번째 노드에서 관리할 값
# count: 건초의 수
# sum  : 방어력의 합
# 오른쪽부터 확인해서 sum이 f(P)를 넘는 최소 X를 처리

# d 좌표압축
n, q = map(int, input().split())
d = list(map(int, input().split()))
d_set = set()
d_set.update(d)
d_map = dict()
d_val = dict()
for i, dx in enumerate(sorted(list(d_set),reverse=True)):
    d_map[dx] = i
    d_val[i] = dx

# 세그트리 초기화
l = len(d_set)
size = 1
while size < l:
    size <<= 1
seg_cnt = [0] * size * 2
seg_sum = [0] * size * 2

# 쿼리 오프라인화
query = []
res = []
for i in range(q):
    x, p = map(int, input().split())
    query.append((x-1, p, i))
query.sort()

# 오프라인 쿼리 처리
idx = -1
for x, p, i in query:
    # 세그트리 갱신
    while x > idx:
        idx += 1
        d_idx = d_map[d[idx]]+size
        while d_idx:
            seg_cnt[d_idx] += 1
            seg_sum[d_idx] += d[idx]
            d_idx >>= 1

    # f(x,p)값 찾기
    node, prefix, cnt = 1, 0, 0
    if seg_sum[node] < p:
        cnt = -1
    else:
        while node < size:
            if seg_sum[node*2] + prefix < p:
                prefix += seg_sum[node*2]
                cnt += seg_cnt[node*2]
                node <<= 1
                node += 1
            else:
                node <<= 1
        cnt += (p-prefix+d_val[node-size]-1)//d_val[node-size]
    res.append((i,cnt))

res.sort()
result = []
for i, r in res:
    result.append(str(r))
print('\n'.join(result))
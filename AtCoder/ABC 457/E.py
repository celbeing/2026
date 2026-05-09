n, m = map(int, input().split())
left, right = [], dict()
left_set = set()
right_set = set()
for _ in range(m):
    l, r = map(int, input().split())
    left.append((l, r))
    right.append((r, l))
    left_set.add(l)
    right_set.add(r)
left.sort()
right.sort()

q = int(input())
query = []
for i in range(q):
    s, t = map(int, input().split())
    query.append((s, t, i))
query.sort()
l = 0
res = [0] * q
for s, t, i in query:
    if not(s in left_set and t in right_set):
        continue
    while left[l][0] < s:
        l += 1
    while l < len(left) - 1 and left[l+1][0] == s and left[l+1][1] <= t:
        l += 1


tk = []
for _ in range(int(input())):
    h, l = map(int, input().split())
    tk.append((l, h))
tk.sort(reverse=True)
tl = []
max_h = 0
for l, h in tk:
    tl.append((l, max_h))

    if max_h < h:
        max_h = h
tl.reverse()

q = int(input())
t = list(map(int, input().split()))
query = []
for i in range(q):
    query.append((t[i],i))
query.sort()
idx = 0
k = max_h
for ti, i in query:
    while tl[idx][0] <= ti:
        k = tl[idx][1]
        idx += 1
    t[i] = k

for p in t:
    print(p)
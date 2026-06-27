h, w = map(int, input().split())
image = [input().strip() for _ in range(h)]
l, r, u, d = w, w, h, h
for i in range(h):
    count = 0
    for j in range(w):
        if image[i][j] == '.':
            count += 1
        else: break
    l = min(l, count)
for i in range(h):
    count = 0
    for j in range(w-1, -1, -1):
        if image[i][j] == '.':
            count += 1
        else: break
    r = min(r, count)
for j in range(w):
    count = 0
    for i in range(h):
        if image[i][j] == '.':
            count += 1
        else: break
    u = min(u, count)
for j in range(w):
    count = 0
    for i in range(h-1, -1, -1):
        if image[i][j] == '.':
            count += 1
        else: break
    d = min(d, count)
for i in range(u, h-d):
    print(image[i][l:w-r])
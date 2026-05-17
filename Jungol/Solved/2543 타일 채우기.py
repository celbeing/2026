n = int(input())
x,y = map(int, input().split())

tile = [[()],[(0,-1),(0,0),(-1,0)],[(-1,-1),(0,-1),(0,0)],[(-1,-1),(-1,0),(0,0)],[(-1,-1),(-1,0),(0,-1)]]
grid = [[0] * n for _ in range(n)]
i = j = n//2

def do_tile(a, b, d):
    for p, q in tile[d]:
        grid[a+p][b+q] = d

def flush(a, b, w):
    if w == 2: return

    if x < a:
        if y < b:
            flush(a-w//4, b-w//4, w//2)
            flat(a, b, w//2, 1)
            flat(a-w//4, b+w//4, w//2, 3)
            flat(a+w//4, b-w//4, w//2, 2)
            flat(a+w//4, b+w//4, w//2, 1)
        else:
            flush(a-w//4, b+w//4, w//2)
            flat(a, b, w//2, 2)
            flat(a-w//4, b-w//4, w//2, 4)
            flat(a+w//4, b-w//4, w//2, 2)
            flat(a+w//4, b+w//4, w//2, 1)
    else:
        if y < b:
            flush(a+w//4, b-w//4, w//2)
            flat(a, b, w//2, 3)
            flat(a-w//4, b-w//4, w//2, 4)
            flat(a-w//4, b+w//4, w//2, 3)
            flat(a+w//4, b+w//4, w//2, 1)
        else:
            flush(a+w//4, b+w//4, w//2)
            flat(a, b, w//2, 4)
            flat(a-w//4, b-w//4, w//2, 4)
            flat(a-w//4, b+w//4, w//2, 3)
            flat(a+w//4, b-w//4, w//2, 2)

def flat(a, b, w, d):
    if w == 2:
        do_tile(a, b, d)
        return
    flat(a, b, w//2, d)
    if d == 1:
        flat(a-w//4, b+w//4, w//2, 3)
        flat(a+w//4, b-w//4, w//2, 2)
        flat(a+w//4, b+w//4, w//2, 1)
    elif d == 2:
        flat(a-w//4, b-w//4, w//2, 4)
        flat(a+w//4, b-w//4, w//2, 2)
        flat(a+w//4, b+w//4, w//2, 1)
    elif d == 3:
        flat(a-w//4, b-w//4, w//2, 4)
        flat(a-w//4, b+w//4, w//2, 3)
        flat(a+w//4, b+w//4, w//2, 1)
    else:
        flat(a-w//4, b-w//4, w//2, 4)
        flat(a-w//4, b+w//4, w//2, 3)
        flat(a+w//4, b-w//4, w//2, 2)

flush(n//2, n//2, n)
if x & 1:
    if y & 1:
        do_tile(x, y, 4)
    else:
        do_tile(x, y+1, 3)
else:
    if y & 1:
        do_tile(x+1, y, 2)
    else:
        do_tile(x+1, y+1, 1)
for i in range(n):
    print(*grid[i])
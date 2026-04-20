n = int(input())
r, c = map(int, input().split())
if n & 1 and (r+c) & 1:
    print(-1, -1)
    exit()
d = [(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]
deg = [[8] * n for _ in range(n)]
check = [[1] * n for _ in range(n)]
deg[0][0] = deg[0][-1] = deg[-1][0] = deg[-1][-1] = 2
deg[0][1] = deg[0][-2] = deg[1][0] = deg[1][-1] = deg[-2][0] = deg[-2][-1] = deg[-1][1] = deg[-1][-2] = 3
deg[1][1] = deg[1][-2] = deg[-2][1] = deg[-2][-2] = 4
for i in range(2, n-2):
    deg[0][i] = deg[-1][i] = deg[i][0] = deg[i][-1] = 4
    deg[1][i] = deg[-2][i] = deg[i][1] = deg[i][-2] = 6

path = [f'{r} {c}']
r-=1;c-=1
check[r][c] = 0

for _ in range(n*n-1):
    min_deg, dist, nxt_r, nxt_c = 8, n*2, -1, -1
    for dx, dy in d:
        nx, ny = r + dx, c + dy
        if 0<=nx<n and 0<=ny<n and check[nx][ny]:
            deg[nx][ny] -= 1
            if min_deg > deg[nx][ny]:
                min_deg = deg[nx][ny]
                dist =  min(nx, n-nx-1) + min(ny, n-ny-1)
                nxt_r, nxt_c = nx, ny
            elif min_deg == deg[nx][ny] and dist > min(nx, n-nx-1) + min(ny, n-ny-1):
                min_deg = deg[nx][ny]
                dist = min(nx, n - nx - 1) + min(ny, n - ny - 1)
                nxt_r, nxt_c = nx, ny

    r, c = nxt_r, nxt_c
    check[r][c] = 0
    path.append(f'{r+1} {c+1}')

print('\n'.join(path))
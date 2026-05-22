from collections import deque
d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
n = int(input())
gdx, gdy, gdhx, gdhy = map(int, input().split())
gsx, gsy, gshx, gshy = map(int, input().split())
gdx-=1;gdy-=1;gdhx-=1;gdhy-=1
gsx-=1;gsy-=1;gshx-=1;gshy-=1
grid = [list(map(int, input().split())) for _ in range(n)]
check = set()
check.add((gdx,gdy,gsx,gsy))
bfs = deque([(gdx,gdy,gsx,gsy,0)])
while bfs:
    p,q,r,s,time = bfs.popleft()
    if p == gdhx and q == gdhy and r == gshx and s == gshy:
        print(time)
        break

    for dx, dy in d:
        np,nq = p+dx,q+dy
        if 0 <= np < n and 0 <= nq < n and grid[np][nq] == 0:
            for tx, ty in d:
                nr, ns = r+tx,s+ty
                if 0 <= nr < n and 0 <= ns < n and grid[nr][ns] == 0 and not(max(abs(nr-np),abs(ns-nq)) <= 1) and not((np,nq,nr,ns) in check):
                    bfs.append((np,nq,nr,ns,time+1))
                    check.add((np,nq,nr,ns))
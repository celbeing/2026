h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]

count = 0
for r in range(1, h+1):
    for c in range(1, w+1):
        for i in range(h+1-r):
            for j in range(w+1-c):
                flag = False
                for a in range(r):
                    for b in range(c):
                        if grid[i+a][j+b] != grid[i+r-1-a][j+c-1-b]:
                            flag = True
                            break
                    if flag: break

                if flag == False:
                    count += 1

print(count)
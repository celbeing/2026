e, w = 0, 0
for k in input().strip():
    if k == 'E':
        e += 1
    else:
        w += 1
if e > w: print('East')
else: print('West')
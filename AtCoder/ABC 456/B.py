four = [0] * 3
five = [0] * 3
six = [0] * 3
for k in list(map(int, input().split())):
    if k == 4: four[0] += 1
    elif k == 5: five[0] += 1
    elif k == 6: six[0] += 1
for k in list(map(int, input().split())):
    if k == 4: four[1] += 1
    elif k == 5: five[1] += 1
    elif k == 6: six[1] += 1
for k in list(map(int, input().split())):
    if k == 4: four[2] += 1
    elif k == 5: five[2] += 1
    elif k == 6: six[2] += 1

res = 0
res += four[0]*five[1]*six[2]
res += four[0]*five[2]*six[1]
res += four[1]*five[0]*six[2]
res += four[1]*five[2]*six[0]
res += four[2]*five[0]*six[1]
res += four[2]*five[1]*six[0]
print(res/(6**3))
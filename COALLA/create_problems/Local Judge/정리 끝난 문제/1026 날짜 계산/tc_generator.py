from random import random, randint
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\1026 날짜 계산\\"

for tc in range(1, 21):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    m = randint(3, 4)
    d, k = 0, randint(1, 30)
    if m == 3:
        d = randint(1, 31)
    else:
        d = randint(1, 30)
    w = file.writelines(f'{m} {d} {k}\n')

    d += k
    if m == 3 and d > 31:
        m += 1
        d -= 31
    elif m == 4 and d > 30:
        m += 1
        d -= 30

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{m}월 {d}일\n')
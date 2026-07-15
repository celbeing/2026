from random import random, randint, shuffle
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\1029 혈액형\\"

type = {0:'O', 1:'A', 2:'B'}
case = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
shuffle(case)
for tc in range(1, 10):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a, b = case.pop()

    w = file.writelines(f'{type[a]} {type[b]}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{'AB' if a*b == 2 else ('O' if a+b == 0 else ('A' if a == 1 or b == 1 else 'B'))}\n')
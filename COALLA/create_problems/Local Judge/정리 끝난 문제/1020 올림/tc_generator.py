import random
from math import ceil
random.random()
check = set()
path = r"/COALLA/create_problems/Local Judge/정리 끝난 문제/1020 올림\\"

for tc in range(1, 11):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a = random.randint(10, 1000000)
    b = random.randint(10, a)
    c = random.randint(10, a)
    while (a, b, c) in check:
        a = random.randint(10, 1000000)
        b = random.randint(10, a)
        c = random.randint(10, a)
    check.add((a, b, c))
    w = file.writelines(f'{a}\n{b}\n{c}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{ceil(a/b)+ceil(a/c)}\n')
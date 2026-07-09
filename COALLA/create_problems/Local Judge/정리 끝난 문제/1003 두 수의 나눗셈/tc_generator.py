import random
random.random()
check = set()
path = r"/COALLA/create_problems/Local Judge/1004 두 수의 나눗셈 (2)\\"

for tc in range(1, 6):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a = random.randint(0,100000000)
    b = random.randint(1, a//100)
    while (a, b) in check:
        a = random.randint(0, 100000000)
        b = random.randint(1, a//100)

    check.add((a, b))
    w = file.writelines(f'{a}\n{b}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{a/b}\n')
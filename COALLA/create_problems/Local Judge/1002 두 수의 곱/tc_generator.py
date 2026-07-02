import random
random.random()
check = set()
path = r"/COALLA/create_problems/Local Judge/1002 두 수의 곱\\"

for tc in range(1, 11):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a, b = random.randint(1,10000), random.randint(1,10000)
    while (a, b) in check:
        a, b = random.randint(1,10000), random.randint(1,10000)
    check.add((a, b))
    w = file.writelines(f'{a}\n{b}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{a*b}\n')
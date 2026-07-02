import random
random.random()
check = set()
path = r"/COALLA/create_problems/Local Judge/1001 두 수의 차\\"

for tc in range(1, 11):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a, b = random.randint(0,100000000), random.randint(0,100000000)
    while (a, b) in check:
        a, b = random.randint(0,100000000), random.randint(0,100000000)
    check.add((a, b))
    w = file.writelines(f'{a}\n{b}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{a-b}\n')
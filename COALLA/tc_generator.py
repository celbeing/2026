import random
random.random()
check = set()
path = r"C:\Users\kimsd\Documents\GitHub\2026\COALLA\\"

for tc in range(1, 51):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a, b, c = random.randint(-100000000,100000000), random.randint(1,100000000), random.randint(1,100000000)
    while (a, b, c) in check:
        a, b, c = random.randint(-100000000, 100000000), random.randint(1, 100000000), random.randint(1, 100000000)
    check.add((a, b, c))
    w = file.writelines(f'{a}\n{b}\n{c}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{a+b+c}\n')
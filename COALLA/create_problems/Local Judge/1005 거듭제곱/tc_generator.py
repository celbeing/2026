import random
random.random()
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\1005 거듭제곱\\"

for tc in range(1, 11):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a, b = random.randint(-100,100), random.randint(1,10)
    while (a, b) in check:
        a, b = random.randint(-100, 100), random.randint(1, 10)
    check.add((a, b))
    w = file.writelines(f'{a}\n{b}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{a**b}\n')
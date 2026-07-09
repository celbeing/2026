import random
random.random()
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\1021 짝수와 홀수\\"

for tc in range(1, 21):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a = random.randint(1, 10000)
    while a in check:
        a = random.randint(1, 100)
    check.add(a)
    w = file.writelines(f'{a}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{'홀수' if a&1 else '짝수'}\n')
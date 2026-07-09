from random import random, randint
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\문제번호\\"

for tc in range(1, 21):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a = randint(100)
    w = file.writelines(f'{a}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{a}\n')
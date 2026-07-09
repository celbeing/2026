import random
random.random()
check = set()
path = r"/COALLA/create_problems/Local Judge/정리 끝난 문제/1013 합체\\"


for tc in range(1, 11):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    A = random.randint(101, 999)
    B = random.randint(100, A)
    w = file.writelines(f'{A} {B}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{str(A+B)+str(A-B)}\n')
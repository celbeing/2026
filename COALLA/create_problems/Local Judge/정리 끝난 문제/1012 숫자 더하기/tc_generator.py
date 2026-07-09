import random
random.random()
check = set()
path = r"/COALLA/create_problems/Local Judge/정리 끝난 문제/1012 숫자 더하기\\"


for tc in range(1, 11):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    A, B = random.randint(1, 1000), random.randint(1, 1000)
    w = file.writelines(f'{A} {B}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{str(A)+str(B)}\n{A+B}\n')
import random
random.random()
check = set()
path = r"/COALLA/create_problems/Local Judge/정리 끝난 문제/1006 출력\\"

for tc in range(1, 2):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')


    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'Hello, World\n')
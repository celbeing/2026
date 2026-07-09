import random
random.random()
check = set()
path = r"/COALLA/create_problems/Local Judge/정리 끝난 문제/1009 순서 바꿔 출력하기\\"

def make_random_string():
    s = ''
    l = random.randint(1, 10)
    for i in range(l):
        s += chr(random.randint(97, 122))
    return s

for tc in range(1, 11):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    A, B = make_random_string(), make_random_string()
    w = file.writelines(f'{A}\n{B}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{B}\n{A}\n')
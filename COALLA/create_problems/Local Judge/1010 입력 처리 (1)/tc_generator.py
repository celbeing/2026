import random
random.random()
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\1010 입력 처리 (1)\\"

def make_random_string():
    s = ''
    l = random.randint(1, 10)
    for i in range(l):
        s += chr(random.randint(97, 122))
    return s

for tc in range(1, 11):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    A, B, C = make_random_string(), make_random_string(), make_random_string()
    w = file.writelines(f'{A} {B}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{A}\n{B}\n')
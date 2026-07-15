from random import random, randint
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\1027 성적표\\"
def SCORE(s):
    if s >= 90: return 'A'
    elif s >= 75: return 'B'
    elif s >= 60: return 'C'
    elif s >= 40: return 'D'
    else: return 'F'

for tc in range(1, 21):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a = randint(0, 100)
    if a in check:
        a = randint(0, 100)
    check.add(a)

    w = file.writelines(f'{a}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{SCORE(a)}\n')
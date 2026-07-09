from random import random, randint
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\1025 비밀번호 힌트\\"

for tc in range(1, 21):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    p = randint(1,100)
    l = randint(4, 10)
    s = ''
    s2 = ''
    for _ in range(l):
        s += chr(randint(ord('!'), ord('z')))
    if p >= 75:
        s2 = s
    else:
        for _ in range(randint(4, 10)):
            s2 += chr(randint(ord('!'), ord('z')))
    w = file.writelines(f'{s}\n{s2}\n')

    file = open(path + f'{tc}.out', 'w+', encoding='utf-8')
    w = file.writelines(f'{'Yes' if s == s2 else 'No'}\n')

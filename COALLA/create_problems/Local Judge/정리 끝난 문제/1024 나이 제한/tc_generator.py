import random
random.random()
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\1024 나이 제한\\"

for tc in range(1, 21):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a = random.randint(1, 100)
    k = random.randint(1, 100)
    while (a, k) in check:
        a = random.randint(1, 100)
        k = random.randint(1, 100)

    check.add((a, k))
    w = file.writelines(f'{a} {k}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{'Yes' if a >= k else 'No'}\n')
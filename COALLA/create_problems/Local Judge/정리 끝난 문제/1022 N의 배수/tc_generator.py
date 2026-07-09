import random
random.random()
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\1022 N의 배수\\"

count = 0
for tc in range(1, 21):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    n = random.randint(1, 10)
    a = random.randint(1, 100000000)
    if (n, a) in check:
        n = random.randint(1, 10)
        a = random.randint(1, 100000000)

    w = file.writelines(f'{n}\n{a}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    if a % n:
        w = file.writelines(f'No\n')
    else:
        w = file.writelines(f'Yes\n')
        count += 1
print(count)
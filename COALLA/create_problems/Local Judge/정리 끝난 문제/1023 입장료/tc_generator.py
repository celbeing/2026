import random
random.random()
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\1023 입장료\\"

count = 0
for tc in range(1, 21):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    n = random.randint(1, 100)
    k = random.randint(2, 100)
    a = random.randint(10, 50)*100
    b = random.randint(8, (a//100)-1)*100
    if (n, k, a, b) in check:
        n = random.randint(1, 100000)
        k = random.randint(2, 1000)
        a = random.randint(10, 50) * 100
        b = random.randint(8, (a // 100) - 1) * 100
    check.add((n, k, a, b))
    w = file.writelines(f'{n} {k} {a} {b}\n')
    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    if n >= k:
        w = file.writelines(f'{n*b}\n')
        count += 1
    else:
        w = file.writelines(f'{(n+1)*a}\n')
print(count)
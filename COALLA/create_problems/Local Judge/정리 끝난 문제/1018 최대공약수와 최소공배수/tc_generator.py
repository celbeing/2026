import random
from math import gcd, lcm
random.random()
check = set()
path = r"/COALLA/create_problems/Local Judge/정리 끝난 문제/1018 최대공약수와 최소공배수\\"

sieve = [1] * 10000001
prime = []
for i in range(2, 10000001):
    if sieve[i]:
        prime.append(i)
        for j in range(i*i, 10000001, i):
            sieve[j] = 0

P = len(prime)
tc_list = []
for _ in range(5):
    g = random.randint(2, 30)
    a, b = prime[random.randint(0, 8)], prime[random.randint(0, 8)]
    while a == b or (g*a, g*b) in check:
        a, b = prime[random.randint(0, 8)], prime[random.randint(0, 8)]
    A, B = g*a, g*b
    check.add((A, B))

    tc_list.append((A, B, gcd(A, B), lcm(A, B)))

for _ in range(5):
    g = random.randint(31, 1000)
    a, b = prime[random.randint(5, P-1)], prime[random.randint(5, P-1)]
    while a == b or (g * a, g * b) in check:
        a, b = prime[random.randint(0, P-1)], prime[random.randint(0, P-1)]
    A, B = g * a, g * b
    check.add((A, B))

    tc_list.append((A, B, gcd(A, B), lcm(A, B)))

random.shuffle(tc_list)

for tc in range(1, 11):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a, b, g, l = tc_list.pop()
    w = file.writelines(f'{a}\n{b}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{g}\n{l}\n')
import sys
input = sys.stdin.readline

# 뫼비우스 함수 값 전처리
mu = [1] * 50000
sieve = [1] * 50000
prime = []
for i in range(2, 50000):
    if sieve[i]:
        prime.append(i)
        mu[i] = -1

    for p in prime:
        if i * p >= 50000: break
        sieve[i*p] = 0
        if i%p == 0:
            mu[i*p] = 0
            break
        else:
            mu[i*p] = -mu[i]

def count(x):
    ret = 0
    i = 1
    while i*i <= x:
        ret += mu[i] * (x//(i*i))
        i += 1
    return ret

def param_search(n):
    ret = 0
    s, e = 1, n*2
    while s <= e:
        m=(s+e)//2
        if count(m) >= n:
            ret = m
            e = m-1
        else:
            s = m+1
    return ret

while True:
    n = int(input())
    if n == 0: break
    print(param_search(n))